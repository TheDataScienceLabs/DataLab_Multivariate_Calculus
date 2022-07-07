"""
Example use of the TCS34725 Micropython library on the
Raspberry Pi Pico. The library was formerly published
by Adafruit, and is still available at https://github.com/adafruit/micropython-adafruit-tcs34725

To use, connect as:

TCS34725 - Pico
GND - GND
VIN - 3V3(OUT)
SDA - GP8
SCL - GP9
LED - GP15
"""

import time
from machine import I2C, Pin
from tcs34725 import TCS34725

led = Pin(15, Pin.OUT)
led.off()
i2c = I2C(0)
sensor = TCS34725(i2c)

# valid gains are 1, 4, 16, 60
sensor.gain(60)

# valid integration times are  2.4, 4.8, 7.2, ..., 614.4
# (in milliseconds)
sensor.integration_time(240)

while True:
    led.on()
    time.sleep(0.25)
    print('R:{} G:{} B:{} Clear:{}'.format(*sensor.read(raw=True)))
    try:
        print('Temperature:{}\t Luminosity:{}'.format(*sensor.read()))
    except ZeroDivisionError:
        print('nothing visible')
    led.off()
    time.sleep(0.5)

