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

while True:
    for i in range(255):
        my_color = (120,i,120)
        strip.fill(my_color)
        strip.show()
        time.sleep(0.025)
