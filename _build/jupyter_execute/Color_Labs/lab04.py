#!/usr/bin/env python
# coding: utf-8

# <div style="background-color:lightblue">
# <h1><center>
#     The Data Science Labs on <br/>
#      Multivariable Calculus  <br/>
#    <small>by Kindyl King and Mireille Boutin</small>
# </center></h1>
#     </div>

# <h1><center>
#     Laboratory 4:<br/>
#     Using an RGB Color Sensor <br/>
#     <p style="font-size: 16px"> Last Updated on May 10, 2022</p>
# </center></h1>

# <h2 style="color:orange;"><left> Content </left></h2>
# 
# #### Mathematics ###
# - 3 dimensional vectors
# - distance
# 
# ### Programming Skills ###
# - modules
# 
# ### Embedded Systems ###
# - Thonny and MicroPython
# 
# <h2 style="color:orange;"><left> Required Hardware </left></h2> 
# 
# - Raspberry Pi Pico
# - RGB color sensor (TCS3472)
# - OLED display
# 

# ### <span style="background-color:lightblue"> Fill in information below: </span>
# __Name:__ me
# 
# __Email:__ me @ purdue.edu

# ## RGB Color Sensors
# 
# We've done a lot of theoretical work about color from learning about tristiulus vectors and metamers, but now let's investigate a use for the RGB color space. The TCS3472 sensor we will be using can detect color and returns an RGB value. The sensor contains an infrared (IR) blocking filter for increased accuracy. IR light is light that has wavelengths of 800-1000 nm; it is invisible to us since humans only percieve wavelengths in the 400-700 nm range. 

# ## Wiring Instructions
# 
# Please make sure your microcontroller is not plugged to the computer while you are wiring things together. Ask the instructor if you are unsure about your wiring. 
# 
# | OLED | Pico |
# |------|------|
# | GND  | GND  |
# | VCC  | 3V3(OUT) |
# | SCL  | I2C0 SCL  or I2C1 SCL |
# | SDA  | I2C0 SDA  or I2C1 SDA |
#  
# <br>
# 
# | TCS34725 | Pico |
# |------|------|
# | GND  | GND  |
# | VIN  | 3V3(OUT) |
# | SDA  | GP8 |
# | SCL  | GP9 |
# | LED  | GP15 | <\span>

# ### <span style="color:red">Exercise</span>
# 
# It's long been debated whether different color M&Ms taste different [[1]](https://www.mashed.com/748770/the-absolute-best-desserts-in-the-us/). Let's say you have a friend who is color blind who wants to test this theory themselves, but it's a challenge to sort red from green from brown M&Ms. To solve this critial problem, your goal is to create an M&M sorter using your Pico and the TCS3472 color sensor. Connect the color sensor and an OLED display to your Pico. When you hold up an M&M to the sensor, the screen should display the name of the color of the M&M.
# 
# 
# __*Hint 1:*__ See example.py in the folder called color_sensor for how to use the sensor. Make sure tcs34725.py is stored on the Pico before you run the example file.
# 
# __*Hint 2:*__ It may be helpful to use the distance between the RGB vector output and "target" colors to detect red, blue, etc. 
# 
# Describe in a few sentences how well your M&M sorter works. Display all code you wrote either by copying and pasting or reading in and printing python file contents. 
# 
# ### <span style="background-color:lightblue">Answer</span>

# In[1]:


# add code


# __

# ## <span style="color:green">Reflection</span>
# 
# __1. What parts of the lab, if any, do you feel you did well? <br>
# 2. What are some things you learned today? <br>
# 3. Are there any topics that could use more clarification? <br>
# 4. Do you have any suggestions on parts of the lab to improve?__
# 
# ### <span style="background-color:lightblue">Answer</span>
