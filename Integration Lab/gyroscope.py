from machine import Pin, I2C
from lsm9ds0 import LSM9DS0
import time
from averager_solution import Averager

i2c = I2C(id=1, sda=Pin(18), scl=Pin(19), freq=3_400_000)
lsm = LSM9DS0(i2c = i2c, a_sens=16)

samples = 50
av_a = Averager(samples)
av_b = Averager(samples)
av_c = Averager(samples)

fileg = open("avged_gyro.txt", "w")

while True:
    a, b, c = lsm.gyro.all()
    av_a.append(a)
    av_b.append(b)
    av_c.append(c)
    fileg.write('{} {} {}\n'.format(av_a.get(),av_b.get(),av_c.get()) )
    print('collecting...')
    time.sleep(0.01)