import numpy as np
import matplotlib.pyplot as plt


def ellipse_function(macroaxis, brachyaxis):
    # Parameter of 'ellipse'
    a = macroaxis  # macroaxis
    b = brachyaxis  # brachyaxis

    # Create Angle array
    theta = np.linspace(0, 2 * np.pi, 100)

    # Parametric equations for ellipses
    x = a * np.cos(theta)
    y = b * np.sin(theta)

    return x, y
