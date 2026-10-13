from flask import Flask, render_template, request
import RPi.GPIO as GPIO
import time

app = Flask(__name__)
# ---------------- GPIO Setup ----------------
GPIO.setmode(GPIO.BCM)
# ---------------- DC MOTOR ----------------
IN1 = 17
IN2 = 27
ENA = 22
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
pwm_dc = GPIO.PWM(ENA, 1000)  # PWM at 1 kHz
pwm_dc.start(0)  # Start with 0% duty cycle

# ---------------- SERVO ----------------
SERVO = 18
GPIO.setup(SERVO, GPIO.OUT)
servo_pwm = GPIO.PWM(SERVO, 50)  # Servo PWM 50 Hz
servo_pwm.start(7.5)  # Neutral position
# ---------------- STEPPER ----------------
step_pins = [5, 6, 13, 19]
for pin in step_pins:
    GPIO.setup(pin, GPIO.OUT)
# Stepper motor sequence for 28BYJ-48
step_seq = [
    [1,0,0,1],
    [1,0,0,0],
    [1,1,0,0],
    [0,1,0,0],
    [0,1,1,0],
    [0,0,1,0],
    [0,0,1,1],
    [0,0,0,1]
]

def step_motor(steps, direction):
    """Rotate the stepper motor a given number of steps in a specified direction."""
    seq = step_seq if direction == 1 else step_seq[::-1]
    for _ in range(steps):
        for step in seq:
            for pin in range(4):
                GPIO.output(step_pins[pin], step[pin])
            time.sleep(0.001)
            
# ---------------- FLASK ROUTES ----------------
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/dc', methods=['POST'])
def dc():
    speed = int(request.form['speed'])
    direction = request.form['direction']
    if direction == "forward":
        GPIO.output(IN1, 1)
        GPIO.output(IN2, 0)
    else:
        GPIO.output(IN1, 0)
        GPIO.output(IN2, 1)
    pwm_dc.ChangeDutyCycle(speed)
    return "DC motor updated"
@app.route('/servo', methods=['POST'])
def servo():
    angle = int(request.form['angle'])
    duty = 2 + (angle / 18)
    servo_pwm.ChangeDutyCycle(duty)
    time.sleep(0.5)
    servo_pwm.ChangeDutyCycle(0)
    return "Servo moved"
@app.route('/stepper', methods=['POST'])
def stepper():
    direction = int(request.form['direction'])
    step_motor(200, direction)  # one full rotation (200 steps for 28BYJ-48)
    return "Stepper moved"

# ---------------- RUN APP ----------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
