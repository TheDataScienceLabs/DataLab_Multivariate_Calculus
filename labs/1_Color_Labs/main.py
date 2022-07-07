"""
This sets a strip of 6 NeoPixels all to the same color
Three colors are displayed in a loop with 0.5 seconds between color changes
"""

import time
from neopixel import Neopixel

numpix = 6
strip = Neopixel(numpix, 0, 0)

color1 = (10, 200, 41)
color2 = (0, 200, 0)
color3 = (56, 56, 56)

#color1 = (206, 184, 136) # Purdue gold looks like grayish white
#color2 = (206, 184, 136)
#color3 = (0, 0, 0)

colors = (color1, color2, color3)

shift = 0
while True:
    shift = (shift+1)%numpix
    for i in range(numpix):
        strip.set_pixel(i, colors[shift%len(colors)])
    strip.show()
    time.sleep(0.5)