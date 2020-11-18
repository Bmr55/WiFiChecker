import time
import RPi.GPIO as GPIO

LED_PIN = 17

def setup_gpio(pin, warnings):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(warnings)
    GPIO.setup(pin, GPIO.OUT)

def turn_on(pin):
    GPIO.output(pin, GPIO.HIGH)

def turn_off(pin):
    GPIO.output(pin, GPIO.LOW)

setup_gpio(LED_PIN, False)
turn_on(LED_PIN)
time.sleep(2)
turn_off(LED_PIN)
