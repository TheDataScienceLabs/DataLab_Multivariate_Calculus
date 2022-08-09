"""a simple script to read numbers off a potentiometer in the planimeter
Wire up the circuit like so:

Pico | 0.1 uF capacitor
GP28 | one leg
GND  | the other

Pico     | Potentiometer
GP28     | wiper
GND      | one pole
3V3(OUT) | other pole

Pico | Button
GP16 | one pin
GND  | other pin

Pico     | OLED
GP4      | SDA
GP5      | SCL
3V3(OUT) | VCC
GND      | GND
"""

from machine import Pin, I2C, ADC
from ssd1306 import SSD1306_I2C
import time


def main():
    i2c = I2C(id=0, sda=Pin(4), scl=Pin(5), freq=1_000_000)
    display = Display(i2c)
    planimeter = ADC(Pin(28))
    button = Pin(16, Pin.IN, Pin.PULL_UP)
    
    reference = 0
    measurements = []
    while True:
        measurements.append(int(planimeter.read_u16()))
        measurements = measurements[-10:]
        now = sum(measurements)/len(measurements)
        if not button.value():
            reference = now
        difference = now - reference
        display.update(reference, now, difference)
        display.show()
        

class Display(SSD1306_I2C):
    def __init__(self, i2c):
        super().__init__(128, 64, i2c)
        self.fill(0)
        self.text("ref:", 0, 0)
        self.text("now:", 0, 12)
        self.text("dif:", 0, 24)
        
    def update(self, reference, now, difference):
        self.fill_rect(32, 0, 128-32, 64, 0)
        self.text(str(reference), 32, 0)
        self.text(str(now), 32, 12)
        self.text(str(difference), 32, 24)
        
    
if __name__ == "__main__":
    main()                                            