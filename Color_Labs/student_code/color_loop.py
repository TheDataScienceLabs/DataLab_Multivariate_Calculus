"""
This is a demo of the Neopixels, using a library published at
https://github.com/blaz-r/pi_pico_neopixel
"""

import time
from neopixel import Neopixel

numpix = 6
strip = Neopixel(numpix, 0, 0,"GRB")

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
colors = (red,green,blue)

shift = 0
while True:
    shift = (shift+1)%numpix
    for i in range(numpix):
        strip.set_pixel(i, colors[(i+shift)%(len(colors))])
    strip.show()
    time.sleep(0.1)
