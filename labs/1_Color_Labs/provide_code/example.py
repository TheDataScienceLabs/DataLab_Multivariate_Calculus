"""
This is a demo of the Neopixels, using a library published at
https://github.com/blaz-r/pi_pico_neopixel
"""



'''
The key methods are set_pixel(n (r,g,b)), 
set_pixel_line(p1, p2, (r, g, b)) which sets a row of pixels from pixel p1 to pixel p2 (inclusive),
and fill((r,g,b)) which fills all the pixels with the color r, g, b. 
'''

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
colors = (red, orange, yellow, green, blue, indigo, violet)

shift = 0
while True:
    shift = (shift+1)%numpix
    for i in range(numpix):
        strip.set_pixel(i, colors[(i+shift)%numpix])
    strip.show()
    time.sleep(0.1)
