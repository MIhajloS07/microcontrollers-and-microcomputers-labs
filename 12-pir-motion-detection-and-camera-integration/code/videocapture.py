import RPi.GPIO as GPIO
import time
import cv2
from datetime import datetime

PIR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

camera = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
print("Video capture initialized...")

try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected - recording video")
            timeT = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            name = f"video_{timeT}.avi"
            out = cv2.VideoWriter(name, fourcc, 20.0, (640, 480))
            start_time = time.time()
            while int(time.time() - start_time) < 10:
                ret, frame = camera.read()
                if ret:
                    out.write(frame)
            out.release()
            print("Video saved:", name)
            time.sleep(5)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopping video capture due to user interruption.")
finally:
    camera.release()
    GPIO.cleanup()
