import time
import RPi.GPIO as GPIO
import os
import picamera
GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN,pull_up_down=GPIO.PUD_UP)
while True:
    input_state=GPIO.input(18)
    if input_state==False:
        camera=picamera.PiCamera()
        camera.capture('/home/pi/Desktop/snapshot.jpg')
        os.system("python /home/pi/Desktop/testing.py /home/pi/Desktop/snapshot.jpg")
        camera.close()
        time.sleep(1)
        
        
        
        
