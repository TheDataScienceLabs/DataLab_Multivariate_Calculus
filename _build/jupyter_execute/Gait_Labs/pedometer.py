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
#     Laboratory on<br/>
#     Gait Detection<br/>
#     <p style="font-size: 16px"> Last Updated on May , 2022</p>
# </center></h1>

# <h2 style="color:orange;"><left> Content </left></h2>
# 
# ### Mathematics ###
# - 3 dimensional vectors
#     
# ### Programming Skills ###
# - modules
#     
# ### Embedded Systems ###
# - Thonny and MicroPython
# 
# <h2 style="color:orange;"><left> Required Hardware </left></h2> 
# 
# - microcontroller: Raspberry Pi Pico
# - breadboard
# - USB connector
# - LSM9DS0 accelerometer
# - OLED display
# - TL1105 tactile switch
# - 9-volt battery
# - 7805 voltage regulator
# 

# ### <span style="background-color:lightblue"> Fill in information below: </span>
# __Name:__ me
# 
# __Email:__ me @ purdue.edu

# ## Storing Data
# 
# The Pico has 2MB onboard memory or flash storage, so we can save some small files of sensor data directly on the Pico. 
# 
# Take a look at the file `temperature.py`, which records the Pico's internal temperature in degrees Celcius and writes these temperature values to the file `temp.txt`.  Using Thonny, run `temperature.py` on your Pico. After the script is done running, move the `temp.txt` file that is stored on the Pico into the folder you are currently working in, delete `temp.txt` from the Pico's storage, and then execute the following cell.

# In[ ]:


import numpy as np
import matplotlib.pyplot as plt

t = np.loadtxt('temp.txt')
plt.plot(t)
plt.show()


# ### <span style="color:red">Exercise</span>
# Plot the values from `temp.txt` so that the x-axis is the time of each measurement and the y-axis is degrees Fahrenheit. Include appropriate x-axis and y-axis labels. 
# ### <span style="background-color:lightblue">Answer</span>

# In[ ]:


# answer here


# ## The Components
# 
# - the button
# - the screen
# - the accelerometer
# - the battery & voltage regulator
# 
# __TODO:__ add instructions from calc 2 labs on how to connect everything

# ## Gait Detection
# 
# Gait is a person's pattern of walking. Most wearable activity monitors like the FitBit or Apple Watch contain an internal accelerometer to track movement and estimate the user's number of steps. In today's lab, our goal is to build a pedometer in a similar way.
# 
# ### <span style="color:red">Exercise</span>
# For this exercise you will only need the accelerometer hooked up to the Pico connected to your computer with the USB connector.
# 1) Take 10 'fake' steps while holding the breadboard with everything secured in your hand, swinging your arms as naturally as possible.
# 1) Store the $x,y,$ and $z$ components of acceleration to a .txt file named `teststeps.txt`.
# 1) Plot the $x,y,$ and $z$ components of acceleration with detailed titles and axis labels.
# 
# ### <span style="background-color:lightblue">Answer</span>

# In[ ]:


# answer here


# In[ ]:


# solution
data = np.loadtxt('teststeps.txt', skiprows=50 )

plt.plot(data[:,0], label='ax(t)')
plt.plot(data[:,1], label='ay(t)')
plt.plot(data[:,2], label='az(t)')
plt.legend()
plt.show()

plt.plot(data)
plt.legend(['ax(t)','ay(t)','az(t)'])
plt.show()


# In order to detect when a step has occured, we will look at the magnitude of the acceleration vector $\langle a_x,a_y,a_z \rangle$, where $a_x,a_y,$ and $a_z$ are the $x,y$ and $z$ components of acceleration respectively.
# 
# ### <span style="color:red">Exercise</span>
# Using the data you collected in `teststeps.txt`, plot the magnitute of the acceleration vector vs time. Make sure your graph has appropriate labels.
# ### <span style="background-color:lightblue">Answer</span>

# In[ ]:


# student answer here


# In[ ]:


# solution
plt.plot(np.linalg.norm(data, axis=1))
plt.show()


# ### <span style="color:red">Exercise</span>
# The class `Averager` allows us to reduce error by averaging across multiple acceleration measurements.
# How does the length of the averager affect the graph of the magnitude of the acceleration vectors?
# ### <span style="background-color:lightblue">Answer</span>

# *student answer here*

# ## Make a Pedometer
# 
# ### <span style="color:red">Exercise</span>
# 
# Let's combine all the components into a useful tool. Make a pedometer with the following features:
# 
# - display the number of steps taken
# - have a "reset" button which starts the step counting back at 0 on the display
# - it should run on battery power alone
# 
# Include a description of your pedometer.
# 
# ### <span style="background-color:lightblue">Answer</span>

# *student answer here*

# ```python
# # copy and paste your code here
# ```

# ## <span style="color:green">Reflection</span>
# 
# __1. What parts of the lab, if any, do you feel you did well? <br>
# 2. What are some things you learned today? <br>
# 3. Are there any topics that could use more clarification? <br>
# 4. Do you have any suggestions on parts of the lab to improve?__
# 
# ### <span style="background-color:lightblue">Answer</span>

# *student answer here*
