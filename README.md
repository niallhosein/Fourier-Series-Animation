# Fourier Series Animation

Welcome to my Fourier Series Animation project! This repository contains Python code utilizing the Manim library to create animated visualizations of Fourier series for a custom function - my name. The animations provide an insightful representation of how Fourier series can approximate complex functions using a combination of sine and cosine terms. 

## Project Overview

### Mathematical Background
While this project is built in such a way that the user would not have to understand most of the underlying mathematics involved, I believe that a brief introduction to the subject is insightful. 

A periodic function can be expressed as an infinite sum of sines and cosines, and this series is called a "Fourier Series". For a periodic function defined on `0 < x < L` with period $P$, the series is given by:

<div align="center">
  
$f(x) = a_0 + \sum_{n=1}^{\infty} \left( a_n \cos\left(\frac{2\pi n x}{P}\right) + b_n \sin\left(\frac{2\pi n x}{P}\right) \right)$

</div>

where:

<div align="center">

$a_0 = \frac{1}{P} \int_{0}^{L} f(x) dx$

$a_n = \frac{2}{P} \int_{0}^{L} f(x) \cos\left(\frac{2\pi n x}{P}\right)dx$

$b_n = \frac{2}{P} \int_{0}^{L} f(x) \sin\left(\frac{2\pi n x}{P}\right)dx$

</div>

_Note: In most cases,_ $P = L$.

Notice that $a_0$ is just the average of the function along the interval `0 < x < L`. This application uses this framework to numerically approximate the Fourier coefficents for a given input function. 

### Getting Started
To run the animations, first define a piecewise function in python that corresponds to the function to be plotted. The following is the function used to generate "NIALL" in the final version:

~~~python
def Niall(self, x):
        x = x % 400 #Implemented to account for periodicity.
        if x < 50:
            return 0
        elif x >= 50 and x <= 100:
            return -2*x + 200
        elif x > 100 and x <=150:
            return 100
        elif x > 150 and x < 200:
            return 0
        elif x >= 200 and x <= 225:
            return 4*x - 800
        elif x > 225 and x <= 250:
            return -4*x + 1000
        elif x > 250 and x <= 300:
            return 0 
        elif x > 300 and x <= 350:
            return 100
        elif x <= 400:
            return 0
~~~

Notice that the function has a period of 400. The first line `x = x % 400` mimics this periodic behaviour for any given input.

Once the animation function has been constructed, change the relevant parameters at the start of the `Construct()` function.

~~~python
 def construct(self):
        low_lim = 0
        upper_lim = 400
        P = 400
        intro_degree = 100
        x_increment = 0.1
        ...
~~~

Given the method used to calculate the fourier coefficients, `low_lim` should remain as 0. The two key parameters that require changes are `upper_lim` and `P` which corresponds to the upper bound of the domain of the function defined and the period of the function respectively. These are both equal in most cases. The value of `upper_lim` can be obtained directly from the animation function constructed.

All other changes can be done by playing around with Manim and observing the results.

### Result

**The following is a 1080p 60fps render of the final result.**


https://github.com/niallhosein/Fourier-Series-Animation/assets/140116446/c3d7c525-b0f7-4271-afd7-b1a496b347e9




## Previous Versions and Preliminary Works
#### Version 0
Initially, I made pre-defined functions and analytically determined the fourier coefficents. I quickly realized that this was very inefficient, and did not allow for much versatility. 

#### Version 1
Having realized that analytically determining the Fourier coefficients was inefficient and not versatile, I opted to numerically approximate the Fourier coefficients. In this version, I decided to animate each letter individually, and combine. 

**Here is the code used to numerically approximate the fourier coefficients:**

~~~python
def calc_a0(self, func, low_lim, upper_lim):        
        result, error = integrate.quad(func, low_lim, upper_lim)
        return result / (upper_lim - low_lim)

def calc_an(self, func, n:int, low_lim, upper_lim):
        result, error = integrate.quad(lambda x: func(x)*np.cos(2*n*np.pi*x / (upper_lim-low_lim)), low_lim, upper_lim)
        return result * 2/(upper_lim - low_lim)

def calc_bn(self, func, n:int, low_lim, upper_lim):
        result, error = integrate.quad(lambda x: func(x)*np.sin(2*n*np.pi*x / (upper_lim-low_lim)), low_lim, upper_lim)
        return result * 2/(upper_lim - low_lim)
~~~

**Here are the preliminary Fourier series representation of each letter.**

<div align="center">

![N](https://github.com/niallhosein/Fourier-Series-Animation/assets/140116446/61b8fddf-15c7-45e4-bf15-4fe77105e2fd)

![I](https://github.com/niallhosein/Fourier-Series-Animation/assets/140116446/651df2de-d26d-4cfb-b801-4d6ad240f819)

![A](https://github.com/niallhosein/Fourier-Series-Animation/assets/140116446/8ac76c87-9c29-4d93-b4b8-23d680876504)

![L](https://github.com/niallhosein/Fourier-Series-Animation/assets/140116446/c1e466f7-f3e1-4eeb-b768-a6ff228176a4)

</div>

_Some letters required two lines to be formed properly. The extra line is shown in orange._

https://github.com/niallhosein/Fourier-Series-Animation/assets/140116446/d2bf4187-384a-4fdf-a890-e7e0d4324855

Notice that it is difficult to see the oscillatory behavior clearly in this version. This is due to:
1) me initially not realizing that for large domains, the x-increment when using Manim should be manually set.
2) the camera being significantly zoomed out.

These considerations, together with me now being more familiar with Manim, led to the development of the final version.

#### Version 2

The primary difference in this version is that I defined the name as one function so that the animation will be closer to the graph to allow the oscillatory behavior to be more easily observered. 

<div align="center">

![Niall](https://github.com/niallhosein/Fourier-Series-Animation/assets/140116446/c3f16559-3989-4dbb-b82a-b4fe015f03f2)

</div>

All other changes are aesthetic using various features provided by the Manim package. 

## Credits
- **Author:** Niall Hosein
- **Background Music:** [Ludwig Göransson - Can You Hear the Music](#)
- **Animation Library:** [Manim Community](https://github.com/ManimCommunity/manim)

Feel free to explore the code, or use this project as a learning resource for Fourier series animations with Manim.

Niall.
