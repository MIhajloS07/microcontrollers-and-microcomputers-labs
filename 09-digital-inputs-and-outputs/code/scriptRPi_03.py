import RPi.GPIO as GPIO
import time

c_led = 18
taster = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(c_led, GPIO.OUT)
GPIO.setup(taster, GPIO.IN, pull_up_down=GPIO.PUD_UP)
led_state = False

def button_pressed(channel):
    global led_state
    led_state = not led_state
    GPIO.output(c_led, led_state)
    print("Button pressed – LED state:", led_state)

GPIO.add_event_detect(
    taster,
    GPIO.FALLING,
    callback=button_pressed,
    bouncetime=300
)

try:
    print("Program running. Press the button to toggle the LED. Press Ctrl+C to exit.")
    while True:
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()