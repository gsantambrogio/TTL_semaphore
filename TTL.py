import RPi.GPIO as GPIO
import time
import gsTTL as gs

# Callback function triggered on signal change
def ttl_callback(channel):
    #do what you need when TTL is detected
    #example:
    state = GPIO.input(channel)
    print(f"TTL Edge Detected! State: {'HIGH' if state else 'LOW'} at {time.time()}")
    gs.TTL_NormalOut(24,1)

gs.TTL_NormalRiIn(23,ttl_callback)

try:
    print("Waiting for TTL pulses... Press Ctrl+C to exit")
    while True:
        time.sleep(1)  # Keep script running

except KeyboardInterrupt:
    print("\nExiting...")

finally:
    GPIO.cleanup()  # Clean up GPIO

