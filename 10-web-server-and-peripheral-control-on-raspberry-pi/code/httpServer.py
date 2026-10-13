import RPi.GPIO as GPIO
from http.server import BaseHTTPRequestHandler, HTTPServer

LED_PIN = 18
# GPIO settings
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

# Web server class inheriting from BaseHTTPRequestHandler
class WebServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/on":
            GPIO.output(LED_PIN, GPIO.HIGH)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"LED ON")
        elif self.path == "/off":
            GPIO.output(LED_PIN, GPIO.LOW)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"LED OFF")
        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open("httpserverIndex.html", "rb") as file:
                self.wfile.write(file.read())
try:
    server = HTTPServer(("0.0.0.0", 8080), WebServer)
    print("Server started on port 8080. Access it via http://<your_pi_ip>:8080")
    server.serve_forever()
except KeyboardInterrupt:
    print("Server stopped by user")
finally:
    GPIO.cleanup()
    server.server_close()