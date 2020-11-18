import time
import RPi.GPIO as GPIO
from check import wifi_connected

LED_PIN = 17

def setup_gpio(pin, warnings):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(warnings)
    GPIO.setup(pin, GPIO.OUT)

def turn_on(pin):
    GPIO.output(pin, GPIO.HIGH)

def turn_off(pin):
    GPIO.output(pin, GPIO.LOW)

def main():
    setup_gpio(LED_PIN, False)
    turn_on(LED_PIN)
    while True:
        is_connected = wifi_connected()
        if is_connected:
            turn_off(LED_PIN)
        else:
            turn_on(LED_PIN)
        time.sleep(5)

if __name__ == "__main__":
    main()
