#gsTTL.py

import RPi.GPIO as GPIO
import time

def TTL_NormalRiIn(pin,ttl_callback):
    TTL_PIN = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TTL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(TTL_PIN, GPIO.RISING, callback=ttl_callback)

def TTL_NormalFaIn(pin,ttl_callback):
    TTL_PIN = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TTL_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(TTL_PIN, GPIO.FALLING, callback=ttl_callback)

def TTL_NormalOut(pin,sec_duration):
    TTL_PIN = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TTL_PIN, GPIO.OUT)
    GPIO.output(TTL_PIN, GPIO.HIGH)
    time.sleep(sec_duration)
    GPIO.output(TTL_PIN, GPIO.LOW)
    
