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
#     Laboratory 5:<br/>
#     Edge Detection in Images <br/>
#     <p style="font-size: 16px"> Last Updated on May 6, 2022</p>
# </center></h1>

# <h2 style="color:orange;"><left> Content </left></h2>
# 
# #### Mathematics ###
# - 3 dimensional vectors
# - Taylor series
# - partial derivatives
# - Second partial derivative test
# - convolution
# ### Programming Skills ###
# - multi-dimensional array manipulation
# - functions
# ### Embedded Systems ###
# - N/A
# 
# <h2 style="color:orange;"><left> Required Hardware </left></h2> 
# 
# - N/A

# ### <span style="background-color:lightblue"> Fill in information below: </span>
# __Name:__ me
# 
# __Email:__ me @ purdue.edu

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


# ## Edge Detection
# 
# Suppose we have a grayscale image and we want to outline all of the objects in the image. We can start by looking for all of the vertical edges in the image. An edge occurs when there is a significant change in intensity. Let's look a very small piece of the grayscale Italy image show in red.
# 

# In[ ]:


import matplotlib.patches as patches

gray_img = np.array(Image.open('gray_italy.jpg'))[:300,:500]

fig, ax = plt.subplots(figsize=(12,6))
ax.imshow(gray_img, cmap='gray')
rect = patches.Rectangle((0, 280), 300, 1, linewidth=0.5, edgecolor='r', facecolor='none')
ax.add_patch(rect)
ax.axis('off')
plt.show()


# By plotting the grayscale values as a 1D function, we can see how the grayscale values change moving down the row from left to right. This function is a bit noisy, but we have seen previously how to smooth it out by taking a rolling average.
# 

# In[ ]:


def rolling_centered_average(x, n):
    out = np.full_like(x, np.nan)
    out[(n - 1) // 2 : -(n // 2)] = np.convolve(x, np.ones(n), mode="valid") / n
    return out

gray_img = np.array(Image.open('gray_italy.jpg'))
slice = gray_img[280:281,:300]

x = gray_img[280,:300]
smoothed = rolling_centered_average(gray_img[280,:300],3)
first_deriv = np.convolve(smoothed[1:-1], np.array([-1,1]), mode="valid")

fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(24, 8),gridspec_kw={'hspace': 0.5})
ax[0].imshow(np.tile(slice,(20,1)), cmap='gray')
ax[0].axis('off')     
ax[0].set_title('Piece of Italy Image Stretched Vertically')  

ax[1].plot(np.arange(0,300),x)
ax[1].plot(np.arange(1,299), smoothed[1:-1])
ax[1].set_xlabel('Column')
ax[1].set_xlim(0,300)
ax[1].set_title('Grayscale Values in Row 280')

ax[2].plot(np.arange(2,299),first_deriv)
ax[2].set_xlabel('Column')
ax[2].set_xlim(0,300)
ax[2].set_title('First Derivative')
plt.show()


# We can see large spikes and dips in the graph of the first derivative where there are abrupt changes in the grayscale values of the row in the image. We can find edges by detecting the local minima and maxima of the first derivative! Since images have two dimensions, a row and column coordinate for each pixel, the example we just went through is a partial derivative.
# 
# Let $f(x,y)$ be a continuous grayscale image mapping $\mathbb{R}^2$ to $\mathbb{R}$.
# When we read in an image in Python we are observing a sampling of points of $f(x,y)$ which we will call $f_d(n,m)$.
# So, $
#     f_d(n,m) = f(n\Delta x, m \Delta y).$
# where $\Delta x$ and $\Delta y$ are the sampling distances along the x and y-axis, respectively.
# Taking partial derivatives of $f$ can be approximated by the forward difference formulas, $
#     \begin{align*}
#         \frac{df}{dx}(n\Delta x,m \Delta y) &\approx \frac{f(n\Delta x+\Delta x,m \Delta y)-f(n\Delta x,m \Delta y)}{\Delta x}
#                                                 = \frac{f_d(n+1,m)-f_d(n,m)}{\Delta x} \\
#         \frac{df}{dy}(n\Delta x,m \Delta y) &\approx \frac{f(n\Delta x,m \Delta y+\Delta y)-f(n\Delta x,m \Delta y)}{\Delta y}
#                                                 = \frac{f_d(n,m+1)-f_d(n,m)}{\Delta y}
#     \end{align*}$
# 
# 
# The gradient of $f$ is $
#     \nabla f = \begin{pmatrix}  \frac{df}{dx} \\  \\ \frac{df}{dy}\end{pmatrix}$
# with magnitude $
#     |\nabla f| = \sqrt{\left(\frac{df}{dx}\right)^2 + \left(\frac{df}{dy}\right)^2}$
# and direction $
#     \theta = \arctan \left(\left(\frac{df}{dy}\right) / \left(\frac{df}{dx}\right)\right).$

# ### <span style="color:red">Exercise</span>
# 
# __Part 1:__ What are the physical interpretations for $|\nabla f|$ and $\theta$?
# 
# __Part 2:__  Plot the magnitute of the gradient of an image.
# 
# __Part 3:__  Pick a threshold for how large the gradient needs to be in order to detect an edge. Justify your choice. 
# 
# __Part 4:__  Plot the edge image so that edge pixels are white and non-edge pixels are black. 
# 
# __Part 5:__ Repeat Parts 2-4 using the symmetric difference formulas for partial derivatives.$
#     \begin{align*}
#         \frac{df}{dx}(n\Delta x,m \Delta y) &\approx \frac{f_d(n+1,m)-f_d(n-1,m)}{2\Delta x} \\
#         \frac{df}{dy}(n\Delta x,m \Delta y) &\approx \frac{f_d(n,m+1)-f_d(n,m-1)}{2\Delta y}
#     \end{align*}$
# 
# __Part 6:__ Describe the differences, if any, between the two edge detectors. 
# 
# ### <span style="background-color:lightblue">Answer</span>
# 

# In[ ]:


# solution
from scipy import signal

gray_img = np.array(Image.open('gray_italy.jpg'))

# PARTS 2-4
dfdy = signal.convolve2d(gray_img, np.array([[-1,1]]), boundary='symm', mode='same')
dfdx = signal.convolve2d(gray_img, np.array([[1],[-1]]), boundary='symm', mode='same')
mag = (dfdy**2+dfdx**2)**(0.5)

fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(24, 8))
ax[0].imshow(gray_img, cmap='gray')
ax[0].axis('off')     
ax[0].set_title('Original Image')  

ax[1].imshow(dfdy, cmap='gray')
ax[1].axis('off')
ax[1].set_title('df/dy')

ax[2].imshow(dfdx, cmap='gray')
ax[2].axis('off')
ax[2].set_title('df/dx')

ax[3].imshow(mag, cmap='gray')
ax[3].axis('off')
ax[3].set_title('Magnitude of Gradient')
plt.show()

thresh = np.quantile(mag,q=.85)
print(thresh)
plt.imshow(mag > thresh, cmap='gray')
plt.axis('off')
plt.show()

# PART 5
dfdy = signal.convolve2d(gray_img, np.array([[-1,0,1]]), boundary='symm', mode='same') / 2
dfdx = signal.convolve2d(gray_img, np.array([[1],[0],[-1]]), boundary='symm', mode='same') / 2
mag = (dfdy**2+dfdx**2)**(0.5)

fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(24, 8))
ax[0].imshow(gray_img, cmap='gray')
ax[0].axis('off')     
ax[0].set_title('Original Image')  

ax[1].imshow(dfdy, cmap='gray')
ax[1].axis('off')
ax[1].set_title('df/dy')

ax[2].imshow(dfdx, cmap='gray')
ax[2].axis('off')
ax[2].set_title('df/dx')

ax[3].imshow(mag, cmap='gray')
ax[3].axis('off')
ax[3].set_title('Magnitude of Gradient')
plt.show()

thresh = np.quantile(mag,q=.85)
print(thresh)
plt.imshow(mag > thresh, cmap='gray')
plt.axis('off')
plt.show()


# The previous exercise has you detect edges based on the first derivative. Another approach is to build an edge detector based on the second derivative because when the second derivative is zero, there is a local minimum or maximum in the first derivative. The strategy is to approximate $\frac{d^2f}{dx^2}, \frac{d^2f}{dxdy}$ and $\frac{d^2f}{dy^2}$ using the information we have available, that is $f_d(n,m)$, and then check where the second derivative changes from positive to negative or vice versa.
# 
# Let's simplify for a moment and see how to approach this in 1 dimension. Suppose $g(x)$ is a continuous function and is infinitely differentiable at the point $a$. The Taylor series of $g(x)$ at $a$ is $
#     g(x) = g(a) + \frac{g'(a)}{1}(x-a) + \frac{g''(a)}{1\cdot 2}(x-a)^2 + \frac{g'''(a)}{1\cdot 2\cdot 3}(x-a)^3 + \cdots  $
# This sum goes on forever, but if we truncate after a few terms we can get a good estimation of the function $g(x)$ near $a$.
# Say we want to approximate $g'(a)$.
# By evaluating $g(x)$ at $x=a+h$ and $x=a-h$ where $h>0$ is a small positive number and only keeping the first two terms in the Taylor series, $
#     \begin{align*}
#         g(a+h) &\approx g(a) + \frac{g'(a)}{1}((a+h)-a) = g(a) + g'(a)h\\
#         g(a-h) &\approx g(a) + \frac{g'(a)}{1}((a-h)-a) = g(a) - g'(a)h\\
#     \end{align*}$
# Now, subtract $g(a+h)$ and $g(a-h)$ to get $
#     g(a+h) - g(a-h) \approx 2g'(a)h \quad \Rightarrow \quad g'(a) \approx \frac{g(a+h)-g(a-h)}{2h},$
# which is the same symmetric difference formula you've seen before.
# To approximate the second derivative $g''(a)$, use the estimations $
#     \begin{align*}
#         g(a+h) &\approx g(a) + \frac{g'(a)}{1}((a+h)-a) + \frac{g''(a)}{1\cdot 2}((a+h)-a)^2 = g(a) + g'(a)h + g''(a)h^2 \\
#         g(a-h) &\approx g(a) + \frac{g'(a)}{1}((a-h)-a) + \frac{g''(a)}{1\cdot 2}((a-h)-a)^2 = g(a) - g'(a)h + g''(a)h^2 \\
#     \end{align*}$
#     
# 

# ### <span style="color:red">Exercise</span>
# 
# Finish the derivation of the estimation of $g''(a)$. Your estimation should only depend on function values of $g$.
# 
# ### <span style="background-color:lightblue">Answer</span>
# 

# *student answer here*

# 
# Going back to the 2-dimensional case, the Taylor series of the funtion $f(x,y)$ at the point $(a,b)$ is $
#     f(x,y) = f(a,b) + (x-a)\frac{df}{dx}(a,b) + (y-b)\frac{df}{dy}(a,b) + 
#         \frac{(x-a)^2\frac{d^2f}{dx^2}(a,b) + 2(x-a)(y-b)\frac{d^2f}{dxdy}(a,b) + (y-b)^2\frac{d^2f}{dy^2}(a,b)}{1 \cdot 2} + \cdots$
# 
# The second partial derivative test states that $f(x,y)$ has a local minimum, local maximum, or saddle point at the point $(a,b)$ if $
#     \left[\frac{d^2f}{dx^2}(a,b) \right] \left[\frac{d^2f}{dy^2}(a,b) \right] - \left[\frac{d^2f}{dxdy}(a,b) \right]^2 = 0.$
# 
# Similar to the 1-dimensional case, we can use Taylor series to derive approximations for $\frac{d^2f}{dx^2},\frac{d^2f}{dy^2}$ and $\frac{d^2f}{dxdy}$.
# 
# For $\frac{d^2f}{dx^2}$, evaluate $f$ at $(x,y)=(a+h,b)$ and $(x,y)=(a-h,b)$ where $h>0$ is a small positive number.
# $\begin{align*}
#     f(a+h,b) &\approx f(a,b) + h\frac{df}{dx}(a,b) + \frac{h^2\frac{d^2f}{dx^2}(a,b)}{2} \\
#     f(a-h,b) &\approx f(a,b) - h\frac{df}{dx}(a,b) + \frac{h^2\frac{d^2f}{dx^2}(a,b)}{2} \\
#     \Rightarrow f(a+h,b)+f(a-h,b) &\approx 2f(a,b) + h^2\frac{d^2f}{dx^2}(a,b) \\
#     \Rightarrow \frac{d^2f}{dx^2}(a,b) &\approx \frac{f(a+h,b)+f(a-h,b)-2f(a,b)}{h^2}
# \end{align*}$
# 

# ### <span style="color:red">Exercise</span>
# 
# Derive the estimations of $\frac{d^2f}{dy^2}$ and $\frac{d^2f}{dxdy}$. Your estimations should only depend on function values of $f$.
# 
# ### <span style="background-color:lightblue">Answer</span>

# *student answer here*

# ### <span style="color:red">Exercise</span>
# 
# Take a photo with your phone or find an image online. Use the second order method to detect edges in the image. Compare the result to the other first-order edge detectors you implemented in a previous exercise.
# 
# 
# ### <span style="background-color:lightblue">Answer</span>
# 

# In[ ]:


# student answer here


# ## <span style="color:green">Reflection</span>
# 
# __1. What parts of the lab, if any, do you feel you did well? <br>
# 2. What are some things you learned today? <br>
# 3. Are there any topics that could use more clarification? <br>
# 4. Do you have any suggestions on parts of the lab to improve?__
# 
# ### <span style="background-color:lightblue">Answer</span>
