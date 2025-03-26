import RPi.GPIO as GPIO
import time

# Pin configuration
LED_PIN = 18  # Change this to your desired GPIO pin

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED on
        print("LED ON")
        time.sleep(1)  # Wait 1 second
        GPIO.output(LED_PIN, GPIO.LOW)   # Turn LED off
        print("LED OFF")
        time.sleep(1)  # Wait 1 second
except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # Reset GPIO settings
