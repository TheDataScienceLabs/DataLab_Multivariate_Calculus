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
import random


numpix = 6
strip = Neopixel(numpix, 0, 0,"GRB")


shift = 0
while True:
    colors = []
    
    for which_pixel in range(6):
        color = []
        for RGB in range(3):
            color.append(random.randint(0,100))
        colors.append(color)
        color = tuple(color)
    colors = tuple(colors)
    print(colors)
            
    shift = (shift+1)%numpix
    for i in range(numpix):
        strip.set_pixel(i, colors[(i+shift)%numpix])
    strip.show()
    time.sleep(0.1)

