"""
This sets a strip of 6 NeoPixels all to the same color
Two colors are displayed in a loop with 1 second between color changes
"""

import time
from neopixel import Neopixel

numpix = 6
strip = Neopixel(numpix, 0, 0)

color1 = (206, 184, 136) # Purdue gold looks like grayish white
color2 = (140, 102, 44) # gamma corrected values with gamma=2.8 
color3 = (159, 124,  64) # gamma corrected values with gamma=2.2


colors = (color1, color2, color3)

shift = 0
while True:
    shift = (shift+1)%numpix
    for i in range(numpix):
        strip.set_pixel(i, colors[shift%len(colors)])
    strip.show()
    time.sleep(3)


