import cv2
import numpy as np
import datetime
import time
from time import sleep
import RPi.GPIO as GPIO
from message import send_to_telegram

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
cap = cv2.VideoCapture(0)

def servo_berputar():
    try:
        servoPIN = 19
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        GPIO.setwarnings(False)
        p = GPIO.PWM(servoPIN, 50)
        p.start(0)
        repeat = 3
        while repeat > 0:
            p.ChangeDutyCycle(2)
            print(datetime.datetime.now)
            time.sleep(0.5)
            p.ChangeDutyCycle(6)
            time.sleep(0.5)
            repeat = repeat - 1
    except:
        p.stop()
        GPIO.stop()
        
def bunyi_buzzer():
    try:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        buzzer=21
        GPIO.setup(buzzer,GPIO.OUT)
        repeat = 3
        while repeat > 0:
            GPIO.output(buzzer,GPIO.HIGH)
            time.sleep(0.5) 
            GPIO.output(buzzer,GPIO.LOW)
            time.sleep(0.5)
            repeat = repeat - 1
    except:
        GPIO.cleanup()
    
merem = 0
print("alat dimulai pukul ")
print(datetime.datetime.now())

while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)
        matadetected = False
        
        if len(faces) > 0:
            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            if len(eyes) == 0:
                merem = merem + 1
                if merem > 2:
                    bunyi_buzzer()

                if merem > 4:
                    servo_berputar()
                    send_to_telegram("Target Mengantuk")
                    print("target mengantuk")
            else:
                GPIO.cleanup()
       

        cv2.imshow('img',img)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break


cap.release()
cv2.destroyAllWindows()
