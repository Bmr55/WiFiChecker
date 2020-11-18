# WiFiChecker
Checks for a WiFi connection on a RPi 3 and displays the result via an LED (ON = No WiFi)

Uses GPIO 17 (PIN #11)

## rc.local
```sudo -H -u pi python3 /home/pi/WiFiChecker/run.py &```
