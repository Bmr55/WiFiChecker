import time
from led import setup_gpio, turn_on, turn_off
from check import wifi_connected

LED_PIN = 17

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
