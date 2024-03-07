# Fourier Series Animation (Work in Progress)

Welcome to my Fourier Series Animation project! This repository contains Python code utilizing the Manim library to create animated visualizations of Fourier series for a custom function - my name. The animations provide an insightful representation of how Fourier series can approximate complex functions using a combination of sine and cosine terms. 

## Project Overview

### Features
- **Custom Function Visualization:** Animate the Fourier series for a custom function, providing a dynamic and intuitive understanding of the approximation process.
- **Degree Variation:** Explore how increasing the degree of the Fourier series impacts the accuracy of the function approximation.
- **Interactive Elements:** Witness the animation of Fourier series graphs, degree counters, and other interactive elements for enhanced visualization.

### Getting Started
To run the animations and explore the functionalities of this project, follow the setup and usage instructions in the documentation.

### Result

https://github.com/niallhosein/Fourier-Series-Animation/assets/140116446/f0d06bcd-e2e6-4fd1-bb02-93b993795ef8



## Previous Versions and Preliminary Works
#### Version 0
Initially, I made pre-defined functions and analytically determined the fourier coefficents. I quickly realized that this was very inefficient, and did not allow for much versatility. 

#### Version 1
Having realized that anayltucally determining the fourier coeffeicents was ineffieicent and not versatile, I opted to numerically approximate the fourier coeffcients. In this version, I decided to animate each letter indivually, and combine. Notice that it is difficult to see the oscillating behaviour cleary in this version. This is due to: 
1) I initially did not realize that for large domains, the x-increment when using Manim should be manually set.
2) The camera is significantly zoomed out.

These considersations, together with me now being more familiar with Manim, led to the development of the final version.

https://github.com/niallhosein/Fourier-Series-Animation/assets/140116446/d2bf4187-384a-4fdf-a890-e7e0d4324855

#### Version 2


## Credits
- Author: Niall Hosein
- Background Music: [Ludwig Göransson - Can You Hear the Music](#)

Feel free to explore the code, or use this project as a learning resource for Fourier series animations with Manim.

Niall.
