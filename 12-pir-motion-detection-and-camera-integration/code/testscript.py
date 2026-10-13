import RPi.GPIO as GPIO
import time
PIR_PIN = 17 # digital input pin for PIR sensor
GPIO.setmode(GPIO.BCM) # processor pin numbering
GPIO.setup(PIR_PIN, GPIO.IN)
print("Test PIR sensor...")
try:
    while True:
        if GPIO.input(PIR_PIN):
            print("Motion detected!")
        else:
            print("No motion detected")
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
