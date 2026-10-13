import RPi.GPIO as GPIO
import time

c_led = 18
taster = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(c_led, GPIO.OUT)
GPIO.setup(taster, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(taster) == GPIO.LOW:
            GPIO.output(c_led, GPIO.HIGH)
        else:
            GPIO.output(c_led, GPIO.LOW)
        time.sleep(0.05)
except KeyboardInterrupt:
    GPIO.cleanup()