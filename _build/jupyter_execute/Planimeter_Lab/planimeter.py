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
#     Green's Theorem<br/>
#     <p style="font-size: 16px"> Last Updated on May 1, 2022</p>
# </center></h1>

# <h2 style="color:orange;"><left>00. Content </left></h2>
# 
# ### Mathematics ###
# - Fundamental Theorem of Calculus
# - Fundamental Theorem for Line Integrals
# - Green's Theorem
# - Partial Derivatives
# - Vector Fields
# - Path Integrals
# - Double Integration
#     
# ### Programming Skills ###
# - 
#     
# ### Embedded Systems ###
# - Thonny and MicroPython
# 
# <h2 style="color:orange;"><left>0. Required Hardware </left></h2> 
# 
# - microcontroller: Raspberry Pi Pico
# - breadboard
# - USB connector
# - rotary encoder
# - rolling platform
# - fixed or adjustable arm
# - tracer (like a pencil or pen)
# 

# ### <span style="background-color:lightblue"> Fill in information below: </span>
# __Name:__ me
# 
# __Email:__ me @ purdue.edu

# ## Green's Theorem
# 
# Recall the Fundamental Theorem of Calculus. If the function $f(x)$ is continuous on the closed interval $[a,b]$ and $F'(x)=f(x)$, i.e., $F$ is an antiderivative of $f$, then
# $$ \int_a^b f(x)dx = F(b)-F(a). $$
# 
# We also have seen the Fundamental Theorem for Line Integrals. Suppose the smooth curve $C$ is parameterized by $\mathbf{r}(t), a \leq t \leq b$ and $f$ is differentiable with gradient $\nabla f$. Then,
# $$ \int_C \nabla f(\mathbf{r}) \cdot d\mathbf{r} = \int_a^b \nabla f(\mathbf{r}(t)) \cdot \mathbf{r}'(t) dt = f(\mathbf{r}(b)) - f(\mathbf{r}(a)). $$
# 
# Green's Theorem is an extension of the Fundamental Theorem of Calculus to two dimensions. In a general sense, the theorem relates line integrals to double integrals, and more specifically, Green's theorem tells us that we can calculate a double integral over a region using only information on the boundary of that region. Suppose the region $D$ is bounded by a simple, smooth, closed curve $C$ which is parameterized in a counter-clockwise direction. If the two-dimensional vector field $\mathbf{F}(x,y)=\langle P(x,y),Q(x,y)\rangle$ is such that $P$ and $Q$ have continous partial derivatives on $D$, then
# $$\oint_C \mathbf{F} \cdot dr = \oint_C Pdx+Qdy = \iint_D (Q_x-P_y)dA, $$
# where $Q_x = \frac{\partial Q}{\partial x}$ and $P_y = \frac{\partial P}{\partial y}$.

# ## Planimeters
# 
# One really neat application of Green's Theorem is that we can calculate the area of a region simply by measuring the boundary. A planimeter is an instrument that does exactly this! The first planimeters were invented as early as 1814 due to a need to calculate land area. In the late 19th century, planimeters became more popular, different internal mechanisms were developed, and even specialty planimeters emerged to calculate things like engine horse-power. More modern uses include finding leaf area in botany and measuring the area of cross-sectional regions from MRI images. All planimeters have a tracer point, a pivot point, and a measuring wheel or mechanism that measures rotation. Here are some examples.
# <p align="center">
#     <img src="polar_planimeter.jpg">
#     <img src="rolling_planimeter.jpg">
#     <img src="modern_planimeter.jpg">
# </p>
# 
# The left image is of a polar planimeter. It has two arms and is fixed at one end while the arm with the tracer point is able to move in a circular region around the fixed point. The center image is of a rolling planimeter. This kind of planimeter is able to move freely on a linear path. The right image is of a modern rolling planimeter that is still being produced. 
# 
# Watch this 18 second [animation](https://www.youtube.com/watch?v=qThV6gTaYMI) of a rolling planimeter. Notice that the gray roller only moves forward and backward on a fixed path, and the yellow arm pivots at the point $B$. As the arm pivots, the marked wheel at the back rotates and skids as the tracer point at $A$ follows the red curve. As the tracer follows the curve the marked wheel will rotate some amount. We will prove that the area of the region is length of the tracer arm (the length from $A$ to $B$) multiplied by the total rolling distance of the wheel after the tracer completely follows the curve counter-clockwise.

# ## Why Do Rolling Planimeters Work?
# 
# Later in the lab, we are going to build a rolling planimeter, so let's first understand why these instruments work. To calculate area in two dimensions 
# $$ \text{area of region $D$} = \iint_D 1 \,dA.$$
# 
# Remember in Green's Theorem, $\mathbf{F}(x,y)=\langle P(x,y),Q(x,y)\rangle$ and
# $$\oint_C \mathbf{F} \cdot dr = \oint_C Pdx+Qdy = \iint_D (Q_x-P_y)dA. $$
# 
# So to calculate area, we need a function $\mathbf{F}(x,y)$ such that $Q_x-P_y = 1$. 
# 
# If $\mathbf{F}(x,y)=\langle 0,x \rangle$, then 
# $$ Q_x-P_y = \frac{\partial}{\partial x}(x) - \frac{\partial}{\partial y}(0) = 1-0 = 1.$$
# This leads us to an important result:
# $$ \text{area of region $D$} = \iint_D 1 \,dA = \oint_C Pdx+Qdy = \oint_C xdy.$$

# ### <span style="color:red">Exercise</span>
# In the our proof, we specifically chose $P(x,y)=0$ and $Q(x,y)=x$, but there are infintely many pairs of $P(x,y)$ and $Q(x,y)$ with the property that $Q_x-P_y = 1$.
# Edit this cell to fill in three different pairs of functions $P$ and $Q$ such that $Q_x-P_y = 1$.
# 
# ### <span style="background-color:lightblue">Answer</span>
# 1. $P(x,y) = $, $Q(x,y) = $
# 2. $P(x,y) = $, $Q(x,y) = $
# 3. $P(x,y) = $, $Q(x,y) = $
# 
# 
# 

# We write points on the curve $C$ as ordered pairs $(x,y)$. In the diagram below (from [here](https://openstax.org/books/calculus-volume-3/pages/6-4-greens-theorem)),
# the pivot point is at $(0,Y)$ so the roller moves up and down the $y$-axis. The tracer arm is length $L$ and the distance from the wheel to the pivot is $l$.
# <p align="center">
#     <img height=400 src="derivation.jpg">
# </p>

# Say we move a very small distance counter-clockwise along the curve $C$ from the point $(x,y)$ to $(x+dx,y+dy)$. Then, the pivot point will move from $(0,Y)$ to $(0,Y+dY)$. We want to know how much the measuring wheel turns as a result of this small motion. If we first move the roller forward without moving the tracer arm, then the tracer moves from $(x,y)$ to $(x,y+dY)$. Next, we move the tracer arm by $d \theta$ without moving the roller. Now we are at the point $(x+dx,y+dy).$ The wheel only rolls with motion that is perpendicular to the tracer arm. The distance the wheel rolls is 
# $\begin{align*}
#     \text{total wheel roll} &= \text{wheel roll from translation} + \text{wheel roll from rotation}\\
#     &= \text{distance between the parallel lines} + \frac{d\theta}{2\pi}\cdot 2l\pi \\
#     &= \sin(\phi)dY + ld\theta \\
#     &= \frac{x}{L}dY + ld\theta.
# \end{align*}$
# 
# If we integrate over $C$ the total wheel roll, then
# $$ \oint_C \frac{x}{L}dY + \oint_C l\,d\theta = \frac{1}{L} \oint_C x\,dY + l\oint_C d\theta = \frac{1}{L} \oint_C x\,dY. $$

# ### <span style="color:red">Exercise</span>
# Explain why $$\oint_C d\theta = 0.$$
# ### <span style="background-color:lightblue">Answer</span>

# *student answer here*

# We are almost there. We only need to relate $\frac{1}{L} \oint_C x\,dY$ to the area of $D$, which we found to be $\oint_C xdy$.
# From the diagram, imagine the right triangle formed by the vertices $(0,Y),(x,y)$, and $(0,y)$.
# By the Pythagorean theorem, $$ x^2 + (y-Y)^2 = L^2. $$
# From the mechanical design of a rolling planimeter, the tracer arm never passes behind the roller, so $y \geq Y$ for every point $(x,y)$ on $C$.
# That is, $Y$ is unique given $(x,y)$.
# Differentiating both sides of $x^2 + (y-Y)^2 = L^2$, we get
# $\begin{align*}
#     2x dx + 2(y-Y)(dy-dY) &= 0 \\
#     x dx + (y-Y)(dy-dY) &= 0 \\
#     dy-dY &= -\frac{x}{y-Y}dx \\
#     dY &= dy + \frac{x}{y-Y}dx \\
#     dY &= dy + \frac{x}{\sqrt{L^2-x^2}}dx
# \end{align*}$
# 
# Now, the total amount the wheel rolls is 
# $$ \frac{1}{L} \oint_C x\,dY = \frac{1}{L} \oint_C x\,dy + \frac{1}{L} \oint_C \frac{x^2}{\sqrt{L^2-x^2}}dx. $$

# ### <span style="color:red">Exercise</span>
# Explain why $$ \oint_C \frac{x^2}{\sqrt{L^2-x^2}}dx = 0.$$ (Hint: use Green's Theorem)
# ### <span style="background-color:lightblue">Answer</span>

# *student answer here*

# ### <span style="color:red">Exercise</span>
# Show that the area of $D$ is $L$ times the total wheel roll after tracing the curve $C$ counter-clockwise.
# ### <span style="background-color:lightblue">Answer</span>

# *student answer here*

# Great job! One pretty remarkable fact is that at the end, the wheel placement - the length $l$ - didn't matter at all! Now we know exactly how a rolling planimeter works. The derivation for how polar planimeters calculate area is very similar. The big difference is that the integration is done in polar coordinates instead of Cartesian coordinates.

# ## Building a Planimeter

# - find some sort of rolling platform to put the breadboard on
# - 2 types of rotary encoders in the lab

# ### <span style="color:red">Exercise</span>
# To test out your planimeter, measure some well known shapes like circles, rectangles, etc.
# Describe how close your estimates are to the exact area. 
# ### <span style="background-color:lightblue">Answer</span>

# *student answer here*

# 
# ### <span style="color:red">Exercise</span>
# Print out a map to calculate area of Indiana or some other state/country with a well known land area. Use your planimeter to measure the area. How close are your calculations? Keep in mind the scale of the map you print. 
# 
# ### <span style="background-color:lightblue">Answer</span>

# 

# ## <span style="color:green">Reflection</span>
# 
# __1. What parts of the lab, if any, do you feel you did well? <br>
# 2. What are some things you learned today? <br>
# 3. Are there any topics that could use more clarification? <br>
# 4. Do you have any suggestions on parts of the lab to improve?__
# 
# ### <span style="background-color:lightblue">Answer</span>

# *student answer here*
