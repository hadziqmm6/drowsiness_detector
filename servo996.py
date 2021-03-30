import RPi.GPIO as GPIO
import time

servoPIN = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setwarnings(False)

p = GPIO.PWM(servoPIN, 50)
p.start(0)
def servo_berputar():
    try:
        while True:
            p.ChangeDutyCycle(2)
            time.sleep(0.5)
            p.ChangeDutyCycle(6)
            time.sleep(0.5)
    except:
        p.stop()
        GPIO.stop()

servo_berputar()

