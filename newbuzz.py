import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
buzzer=21
GPIO.setup(buzzer,GPIO.OUT)

def bunyi_buzzer():
    try:
        while True:
            GPIO.output(buzzer,GPIO.HIGH)
            sleep(0.5) # Delay in seconds
            GPIO.output(buzzer,GPIO.LOW)
            sleep(0.5)
    except:
        GPIO.cleanup()
bunyi_buzzer()
