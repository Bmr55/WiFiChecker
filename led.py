import RPi.GPIO as GPIO

def setup_gpio(pin, warnings):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(warnings)
    GPIO.setup(pin, GPIO.OUT)

def turn_on(pin):
    GPIO.output(pin, GPIO.HIGH)

def turn_off(pin):
    GPIO.output(pin, GPIO.LOW)
