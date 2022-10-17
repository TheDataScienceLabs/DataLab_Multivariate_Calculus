"""
Example use of the TCS34725 Micropython library on the
Raspberry Pi Pico. The library was formerly published
by Adafruit, and is still available at https://github.com/adafruit/micropython-adafruit-tcs34725
"""

import time
from machine import Pin, I2C
from tcs34725 import TCS34725, html_rgb
from ssd1306 import SSD1306_I2C

def main():
    i2c = I2C(id=0, sda=Pin(4), scl=Pin(5), freq=1_000_000)
    display = Display(i2c)
    rgb_sensor = TCS34725(i2c)
    sensor_led = Pin(0, Pin.OUT)
    sensor_led.on() # turns on the sensor's led to illuminate the object in front of it
    while True:
        data = rgb_sensor.read(raw=True) # get the sensor's data
        try:
            r,g,b = html_rgb(data) # return RGB values between 0 and 255 of the color detected
            display.update(r,g,b) # displays r,g, and b values to the screen
        except ZeroDivisionError: # prevents program from stoppping if nothing is detected
            display.update("na","na","na") 
        time.sleep(0.25) # every 0.25 seconds we collect the data and display the RGB values

class Display(SSD1306_I2C):
    def __init__(self, i2c):
        super().__init__(128, 64, i2c)
        self.fill(0)
        self.text('loading...', 0, 0, 1)
        self.show()
        
    def update(self, r, g, b):
        self.fill(0)
        self.text(f"r:{r}", 0, 10, 1)
        self.text(f"g:{g}", 0, 20, 1)
        self.text(f"b:{b}", 0, 30, 1)
        self.show()

if __name__ == '__main__':
    main()
