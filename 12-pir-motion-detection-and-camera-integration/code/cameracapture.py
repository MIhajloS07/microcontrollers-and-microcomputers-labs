import RPi.GPIO as GPIO
import time
import cv2
from datetime import datetime

PIR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

camera = cv2.VideoCapture(0)
print("System started...")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")
            ret, frame = camera.read()
            if ret:
                timeT = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                name = f"image_{timeT}.jpg"
                cv2.imwrite(name, frame)
                print(f"Image saved: {name}")
            time.sleep(5)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Interrupted by user")
finally:
    camera.release()
    GPIO.cleanup()
