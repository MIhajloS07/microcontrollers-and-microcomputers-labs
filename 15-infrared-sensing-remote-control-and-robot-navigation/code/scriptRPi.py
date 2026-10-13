import RPi.GPIO as GPIO
import time

IR_PIN = 17
LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(IR_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
pwm_led = GPIO.PWM(LED_PIN, 1000)
pwm_led.start(0)

duty = 0

def read_nec():
    # wait for start LOW (~9ms)
    while GPIO.input(IR_PIN) == 1:
        pass

    t0 = time.perf_counter()
    while GPIO.input(IR_PIN) == 0:
        if time.perf_counter() - t0 > 0.02:
            return None

    # wait for HIGH (~4.5ms)
    t1 = time.perf_counter()
    while GPIO.input(IR_PIN) == 1:
        if time.perf_counter() - t1 > 0.01:
            return None

    bits = []

    for i in range(32):
        # LOW (~560us)
        t_low = time.perf_counter()
        while GPIO.input(IR_PIN) == 0:
            if time.perf_counter() - t_low > 0.002:
                return None

        # HIGH duration determines the bit
        t_high = time.perf_counter()
        while GPIO.input(IR_PIN) == 1:
            if time.perf_counter() - t_high > 0.003:
                break

        duration = time.perf_counter() - t_high

        if duration > 0.001:  # 1 = longer signal
            bits.append(1)
        else:
            bits.append(0)

    # convert to number
    value = 0
    for bit in bits:
        value = (value << 1) | bit
    return value

try:
    print("Waiting for IR signal...")
    while True:
        code = read_nec()
        if code is not None:
            print(f"Received code: {hex(code)}")
            if code == 0xFFFFFFFF:
                continue

            if code == 0xffc23d:  # ON/OFF
                duty = 0 if duty > 0 else 50
                print("LED:", "ON" if duty > 0 else "OFF")

            elif code == 0xffa857:  # +
                duty = min(100, duty + 15)
                print("LED brightness:", duty)
                
            elif code == 0xffe01f:  # -
                duty = max(0, duty - 15)
                print("LED brightness:", duty)
                
            pwm_led.ChangeDutyCycle(duty)
        time.sleep(0.05)
except KeyboardInterrupt:
    GPIO.cleanup()