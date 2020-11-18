import time
from led import setup_gpio, turn_on, turn_off

LED_PIN = 17

def led_test():
    setup_gpio(LED_PIN, False)
    turn_on(LED_PIN)
    time.sleep(2)
    turn_off(LED_PIN)
    
if __name__ == "__main__":
    led_test()
