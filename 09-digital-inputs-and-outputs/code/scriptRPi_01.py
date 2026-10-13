import RPi.GPIO as GPIO
import time

c_led = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(c_led, GPIO.OUT)

try:
    while True:
        GPIO.output(c_led, GPIO.HIGH) # LED ON
        time.sleep(1)
        GPIO.output(c_led, GPIO.LOW) # LED OFF
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()