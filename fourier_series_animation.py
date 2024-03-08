"""
Fourier Series Animation
Author: Niall Hosein
Copyright (c) 2024 Niall Hosein. All rights reserved.

This program uses Manim, a community-driven animation engine for explanatory math videos.
For more information on Manim, visit: https://github.com/ManimCommunity/manim

Background music: "Can You Hear The Music" by Ludwig Göransson
"""

from scipy import integrate
import numpy as np
import matplotlib.pyplot as plt
from manim import *

# export PATH="/usr/local/texlive/2023/bin/universal-darwin:$PATH" Be sure to change the environment variable for latex features.

class Animation(MovingCameraScene):
    """
    A class for animating Fourier series for a custom function on the interval `0 < x < L` using Manim.

    This class extends the Manim Scene class and includes methods for calculating Fourier coefficients,
    generating Fourier series animations, and visualizing the approximation of a custom function.

    Attributes:
        - self.Niall (function): Custom input function for Fourier series animation.
        - self.camera (manim.mobject.camera.ThreeDCamera): Camera for rendering the animation.
    """

    def calc_a0(self, func, low_lim, upper_lim):
        """
        Calculate the constant Fourier term, `a0`.

        This function computes the average value of the input function over the specified domain.

        Args:
            func (callable): The input function.
            low_lim (float): The lower bound of the domain of the function.
            upper_lim (float): The upper bound of the domain of the function.

        Returns:
            float: The calculated constant Fourier term, `a0`.
        """
        
        result, error = integrate.quad(func, low_lim, upper_lim)
        return result / (upper_lim - low_lim)

    def calc_an(self, func, n:int, low_lim, upper_lim):
        """
        Calculate the Fourier coefficient `a_n` for the given order `n`.

        This function computes the `a_n` coefficient for a periodic function represented by the input
        function over the specified domain.

        Args:
            func (callable): The input function.
            n (int): The order of the Fourier coefficient.
            low_lim (float): The lower bound of the domain of the function.
            upper_lim (float): The upper bound of the domain of the function.

        Returns:
            float: The calculated Fourier coefficient `a_n`.
        """

        result, error = integrate.quad(lambda x: func(x)*np.cos(2*n*np.pi*x / (upper_lim-low_lim)), low_lim, upper_lim)
        return result * 2/(upper_lim - low_lim)

    def calc_bn(self, func, n:int, low_lim, upper_lim):
        """
        Calculate the Fourier coefficient `b_n` for the given order `n`.

        This function computes the `b_n` coefficient for a periodic function represented by the input
        function over the specified domain.

        Args:
            func (callable): The input function.
            n (int): The order of the Fourier coefficient.
            low_lim (float): The lower bound of the domain of the function.
            upper_lim (float): The upper bound of the domain of the function.

        Returns:
            float: The calculated Fourier coefficient `b_n`.
        """

        result, error = integrate.quad(lambda x: func(x)*np.sin(2*n*np.pi*x / (upper_lim-low_lim)), low_lim, upper_lim)
        return result * 2/(upper_lim - low_lim)
    
    def calc_coeffs(self, degree, low_lim, upper_lim, func):
        """
        Calculate the Fourier coefficients up to the given degree.

        This function computes the constant term `a0`, and coefficients `a_n` and `b_n` for the given
        degree of the Fourier series representation of the input function over the specified domain.

        Args:
            degree (int): The degree of the Fourier series.
            low_lim (float): The lower bound of the domain of the function.
            upper_lim (float): The upper bound of the domain of the function.
            func (callable): The input function.

        Returns:
            tuple: Tuple containing the constant term `a0`, a list of `a_n` coefficients, and a list
                of `b_n` coefficients.
        """

        a0 = self.calc_a0(func, low_lim, upper_lim)
        a_n = []
        b_n = []
        for n in np.arange(1, degree + 1, 1):
            a_n.append(self.calc_an(func, n, low_lim, upper_lim))
            b_n.append(self.calc_bn(func, n, low_lim, upper_lim))
         
        return a0, a_n, b_n
    
    def fourier_series(self, x, degree, a0, an, bn, P):
        """
        Calculate the Fourier series approximation at a given point.

        This function computes the Fourier series approximation at the specified point `x` using the
        given coefficients.

        Args:
            x (float): The point at which to evaluate the Fourier series.
            degree (int): The degree of the Fourier series.
            a0 (float): The constant term.
            an (list): List of `a_n` coefficients.
            bn (list): List of `b_n` coefficients.
            P (float): The period of the Fourier series.

        Returns:
            float: The Fourier series approximation at the specified point.
        """

        result = 0
        for n in range(degree):
            temp = (an[n]*np.cos(2*(n+1)*np.pi*x / P)) + (bn[n]*np.sin(2*(n+1)*np.pi*x / P))
            result = result + temp
            
        return a0 + result
    
    def plot_graph(self, degree, low_lim, upper_lim, func, func2=None, num_points = 1000):
        """
        Plot the Fourier series approximations of the input function(s).

        This function generates a plot of the Fourier series approximations for the given input function(s).

        Note: The period of the function is assumed to be `upper_lim` - `low_lim`.

        Args:
            degree (int): The degree of the Fourier series.
            low_lim (float): The lower bound of the domain of the function.
            upper_lim (float): The upper bound of the domain of the function.
            func (callable): The input function.
            func2 (callable, optional): Second input function for comparison (default is None).
            num_points (int, optional): Number of points for plotting (default is 1000).

        Returns:
            None: The plot is displayed using Matplotlib.
        """

        a0, an, bn = self.calc_coeffs(degree, low_lim, upper_lim, func)
        if func2 != None: a0_2, an_2, bn_2 = self.calc_coeffs(degree, low_lim, upper_lim, func2)
        
        x = np.linspace(low_lim, upper_lim, num_points)
        func1_fs = self.fourier_series(x, degree, a0, an, bn, upper_lim - low_lim)
        plt.plot(x, func1_fs)

        if func2 != None:
            func2_fs = self.fourier_series(x, degree, a0_2, an_2, bn_2, upper_lim - low_lim)
            plt.plot(x, func2_fs)

        plt.show()

    def Niall(self, x):
        """
        Definition of the custom function 'Niall'.

        Args:
            x (float): The input value.

        Returns:
            float: The output value based on the defined function.
        """

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
        
    def construct(self):
        """
        Animate the Fourier series for Niall's function.

        This function creates an animation to visualize the Fourier series for Niall's function with varying degrees.

        Returns:
            None: The animation is displayed using Manim.
        """

        low_lim = 0
        upper_lim = 400
        P = 400
        intro_degree = 100
        x_increment = 0.1

        # Save the initial state of the camera frame
        self.camera.frame.save_state()

        # Add background music
        self.add_sound("/Users/niallhosein/Desktop/FourierSeriesAnimation/soundtrack.mp3")

        # Wait for 1 second
        self.wait(1)

        # Create the title
        title = Text("Fourier Series for Niall").shift(UP * 3)

        # Create the axes
        axes = Axes(x_range=[0, 415, 415], y_range=[0, 100, 100])

        # Calculate Fourier coefficients for the introductory degree - i.e. the graph that is first shown
        a0, an, bn = self.calc_coeffs(intro_degree, low_lim, upper_lim, self.Niall)

        # Play the animation of drawing the axes
        self.play(DrawBorderThenFill(axes, run_time=1))

        # ValueTracker for animation control - first portion of graph
        alpha = ValueTracker(0)

        # Plot the introductory Fourier series graph
        intro_graph = axes.plot(lambda x: self.fourier_series(x, intro_degree, a0, an, bn, P), color=RED,
                                x_range=[low_lim, 50, x_increment])
        graph_skel = axes.plot(lambda x: self.fourier_series(x, intro_degree, a0, an, bn, P), color=RED,
                            x_range=[low_lim, 400, x_increment])

        # Create a dot that follows the graph
        dot1 = always_redraw(lambda: Dot(intro_graph.point_from_proportion(alpha.get_value())))

        # Scale and move the camera frame
        self.play(self.camera.frame.animate.scale(0.2).move_to(axes.c2p(25, 0)))

        # Draw the introductory graph and dot
        self.play(DrawBorderThenFill(intro_graph))
        self.add(graph_skel)
        self.play(DrawBorderThenFill(dot1), run_time=1)

        # Animate the alpha ValueTracker
        self.play(alpha.animate.set_value(0.8), rate_func=rush_into, run_time=5)

        # Remove the dot1
        self.remove(dot1)

        # Create and animate the beta ValueTracker - middle portion of graph
        beta = ValueTracker(0)
        graph2 = axes.plot(lambda x: self.fourier_series(x, intro_degree, a0, an, bn, P), x_range=[100, 149.7, x_increment],
                        color=RED)
        dot2 = always_redraw(lambda: Dot(graph2.point_from_proportion(beta.get_value())))
        self.play(self.camera.frame.animate.scale(2).move_to(axes.c2p(125, 100)))
        self.add(graph2, dot2)
        self.play(beta.animate.set_value(1), rate_func=smooth, run_time=4)
        self.remove(dot2)

        # Create and animate the gamma ValueTracker - for the final portion of graph
        gamma = ValueTracker(0)
        third_graph = axes.plot(lambda x: self.fourier_series(x, intro_degree, a0, an, bn, P), color=RED,
                                x_range=[226, 332, x_increment])
        dot3 = always_redraw(lambda: Dot(third_graph.point_from_proportion(gamma.get_value())))
        self.play(self.camera.frame.animate.scale(1.5).move_to(axes.c2p(275, 50)))
        self.play(DrawBorderThenFill(third_graph))
        self.add(dot3)
        self.play(gamma.animate.set_value(0.8), rate_func=smooth, run_time=5)
        self.remove(dot2, dot3)

        # Restore the camera frame to its initial state
        self.play(Restore(self.camera.frame))

        # Dummy dot for smooth transitions of objects
        dummy = Dot().set_opacity(0)

        # Remove the introductory graphs
        self.remove(intro_graph, graph2, third_graph, graph_skel)
        self.play(ReplacementTransform(graph_skel, dummy))
        self.play(self.camera.frame.animate.scale(1.3))

        # Set the range for degree values
        set_range = [1, 2, 3, 4, 5, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 95, 100]

        # Iterate through different degrees and plot the corresponding Fourier series graphs
        for i in set_range:
            if i == set_range[0]:
                # Plot the initial Fourier series graph
                a0, an, bn = self.calc_coeffs(i, low_lim, upper_lim, self.Niall)
                G_orig = axes.plot(lambda x: self.fourier_series(x, i, a0, an, bn, P), x_range=[low_lim, upper_lim, x_increment],
                                color=RED)

                # Display the title and degree counter
                title = Text("Fourier Series for Niall").shift(UP * 4.5)
                counter_orig = Tex(r"\textit{n} = " + str(i)).shift(DOWN * 4.5)
                self.play(DrawBorderThenFill(title), DrawBorderThenFill(counter_orig))
                self.play(Create(G_orig))

                continue

            # Plot the subsequent Fourier series graphs
            a0, an, bn = self.calc_coeffs(i, low_lim, upper_lim, self.Niall)
            G_new = axes.plot(lambda x: self.fourier_series(x, i, a0, an, bn, P), x_range=[low_lim, upper_lim, x_increment],
                            color=RED)
            counter_new = Tex(r"\textit{n} = " + str(i)).shift(DOWN * 4)

            # Adds the stroke for A when the degree is 20
            if i == 20:
                line = axes.plot(lambda x: 50, x_range=[212.5, 237.5], color=RED)
                self.play(ReplacementTransform(G_orig, G_new), ReplacementTransform(counter_orig, counter_new), Create(line))
            else:
                self.play(ReplacementTransform(G_orig, G_new), ReplacementTransform(counter_orig, counter_new))

            # Updates for replacement transform to work correctly in the subsequent loop
            G_orig = G_new
            counter_orig = counter_new

        # Wait for 3 seconds
        self.wait(3)

        # Restore the camera frame to its initial state and remove unnecessary elements
        self.play(Restore(self.camera.frame), ReplacementTransform(counter_new, dummy), ReplacementTransform(title, dummy))
