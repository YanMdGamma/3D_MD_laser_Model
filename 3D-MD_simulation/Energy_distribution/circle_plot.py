import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import random

if __name__ == "__main__":

    center_x = 0
    center_y = 0
    # radius = 5

    theta = np.linspace(0, 2 * np.pi, 100)

    step_interval = 0.25
    x_dia = 5

    repeat_ = round(x_dia / step_interval)

    x_all = np.zeros((repeat_, 1))
    y_all = np.zeros((repeat_, 1))

    for i in range(0, repeat_):
        x_all[i] = step_interval + step_interval*(i)
        y_all[i] = step_interval + step_interval * (i)

    plt.figure(figsize=(6, 6))
    for i in range(0, repeat_):

        x = center_x + x_all[i] * np.cos(theta)
        y = center_y + y_all[i] * np.sin(theta)
        sio.savemat(f'./cir/y_cir{i}.mat', {'mydata': y})
        sio.savemat(f'./cir/x_cir{i}.mat', {'mydata': x})

        plt.plot(x, y, color=(random.random(), random.random(), random.random()))
        plt.gca().set_aspect('equal', adjustable='box')
        plt.title('Circle')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.grid(True)

    plt.show()
