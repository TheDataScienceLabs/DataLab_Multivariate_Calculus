from machine import Pin
frequency = 60
duty_circle = 0.5
period = 1/60
count = 0
led = Pin(25,Pin.OUT)
while(1):
    if(count < (60 * duty_circle)):
        led.value(1)
    else:
        led.value(0)
    count = (count + 1) % frequency