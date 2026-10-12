import serial
import threading
import RPi.GPIO as GPIO

# Configure GPIO pin numbering (if needed)
GPIO.setmode(GPIO.BCM)

ser = serial.Serial("/dev/serial0", 9600)


# Receive data from the Arduino
def receive():
    while True:
        try:
            data = ser.readline().decode().strip()
            if data:
                print("[Arduino]:", data)
        except Exception:
            pass


# Start the receiving thread
threading.Thread(target=receive, daemon=True).start()


# Send commands to the Arduino
try:
    while True:
        cmd = input("Command (LED ON / LED OFF / STATUS?): ")
        ser.write((cmd + "\n").encode())

except KeyboardInterrupt:
    GPIO.cleanup()
    ser.close()