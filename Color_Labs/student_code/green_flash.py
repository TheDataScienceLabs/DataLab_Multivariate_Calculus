"""
This is a demo of the Neopixels, using a library published at
https://github.com/blaz-r/pi_pico_neopixel
"""


import time
from neopixel import Neopixel

numpix = 6
strip = Neopixel(numpix, 0, 0,"GRB")


pwd = 0.1
green = (0 , 255  , 0)
green_10_percent = (0 ,255 * pwd,0)

for i in range(6):
    if i % 2 == 0:
        strip.set_pixel(i, green) #set the even indexing neopixel to 100% duty circule red 
    if i % 2 == 1:
        strip.set_pixel(i, green_10_percent) # set the odd indexing neopixel to 10% duty circule red 
   

strip.show()
