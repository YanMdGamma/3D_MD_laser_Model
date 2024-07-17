import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps
import random
import scipy.io as sio

def setLabel(ax,*args):
    ax.set_xlabel(args[0])
    ax.set_ylabel(args[1])
    if len(args) == 3:
        ax.set_zlabel(args[2])
def  GaussGif1d(w0, layer_n, P_ave, t, A, f): # 100W/cm2 100微米 还需要单脉冲激光的加工时间 10微秒
    t = t
    x = np.linspace(-10, 10, 500)  # Coordinate axes are evenly divided

    x_max = w0*2.5
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xlim(-x_max, x_max)
    ax.set_ylim(0, P_ave + 10)
    ax.grid()

    # line, = ax.plot([], [])
    # time_text = ax.text(0.1, 0.9, '', transform=ax.transAxes)

    ave_w0 = float(x_max/layer_n)
    print('ave_w0: \n', ave_w0)

    # # Initialize image
    # def init():
    #     line.set_data([], [])
    #     time_text.set_text("")
    #     return line, time_text

    Psi = np.exp(-x ** 2 / w0 ** 2) * P_ave
    sio.savemat('Psi.mat', {'mydata': Psi})
    sio.savemat('x.mat', {'mydata': x})

    plt.plot(x, Psi, label='ellipse', linewidth=2.0, color=(random.random(), random.random(), random.random()))
    plt.show()
    # 3D plot
    fig3d = plt.figure()
    X3d, Y3d = np.meshgrid(np.linspace(-w0*2.5, w0*2.5, 100), np.linspace(-w0*2.5, w0*2.5, 100))
    Psi3d = np.exp(-(X3d**2+Y3d**2)/w0**2) * P_ave
    ax2 = fig3d.add_subplot(111, projection='3d')
    ax2.plot_surface(X3d, Y3d, Psi3d)
    ax2.set_title("Intensity distribution on waist0")
    setLabel(ax2, "x", "y", "Instensity")
    sio.savemat('Psi3d.mat', {'mydata': Psi3d})
    sio.savemat('X3d.mat', {'mydata': X3d})
    sio.savemat('Y3d.mat', {'mydata': Y3d})
    plt.show()

    P_peak = P_ave/(t*f)
    I0 = 2 * P_peak/(math.pi * w0 ** 2)
    In_TTM_aft = np.zeros((layer_n, 1))
    # print('A: \n', A)
    for i in range(1, layer_n + 1):
        #w = w0   We just pick the Gaussian light distribution in the center
        x_min = 0 + (i - 1)*ave_w0
        x_max = i*ave_w0
        x_values = np.linspace(x_min, x_max, 1000)  # Generates 1000 x values

        # Strength to calculate the absorption of the part
        # Psi = np.exp(-x_values ** 2 / w0 ** 2) * I0 * t * A
        Psi = 2*np.exp(-x_values ** 2 / w0 ** 2) * I0 * t * A
        # print(Psi)

        In_TTM_aft[layer_n - i][0] = simps(Psi, x_values)

    # In_TTM_aft = sorted(In_TTM_aft[1])
    # print(In_TTM_aft)

    return In_TTM_aft


