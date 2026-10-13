# WebSocket server for controlling an LED on Raspberry Pi
import asyncio
import websockets
import RPi.GPIO as GPIO

LED_PIN = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

async def led_control(websocket):
    async for message in websocket:
        if message == "ON":
            GPIO.output(LED_PIN, GPIO.HIGH)
            await websocket.send("LED TURNED ON")
        elif message == "OFF":
            GPIO.output(LED_PIN, GPIO.LOW)
            await websocket.send("LED TURNED OFF")
            
async def main():
    async with websockets.serve(led_control, "0.0.0.0", 8765):
        print("WebSocket server started on port 8765. Connect via ws://<your_pi_ip>:8765")
        await asyncio.Future() # work forever

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Server stopped by user")
finally:
    GPIO.cleanup()