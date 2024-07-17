from Absorption_Energy import calculate_k, absorption_energy
from ellipse_function import ellipse_function
from Gaussian_beam import GaussGif1d
import matplotlib.pyplot as plt
import random
import numpy as np
import sympy as sp
from scipy.integrate import simps
import scipy.io as sio

if __name__=="__main__":
    # Set the shell at a specific distance
    step_interval = 0.25  # Suppose a layer of spherical shell is set at 0.25 μm each time
    # Set the range of laser irradiation x = y, z
    x_dia = 5
    print('x_dia: \n', x_dia)
    z = 6

    repeat_ = round(x_dia/step_interval)
    print('repeat_: \n', repeat_)
    z_step_inte = z/repeat_

    # The longitudinal distance results are homogenized according to the horizontal distance distribution
    x_all = np.zeros((repeat_, 1))
    z_all = np.zeros((repeat_, 1))

    for i in range(0, repeat_):
        x_all[i] = step_interval + step_interval*(i)
        z_all[i] = z_step_inte + z_step_inte*(i)
    print('z:\n', z_all)
        # This is the length of the semi-axis of all the shells
    plt.figure()
    for i in range(0, repeat_):
        x, y = ellipse_function(x_all[i], z_all[i])
        plt.plot(x, y, label='ellipse', linewidth =2.0, color=(random.random(), random.random(), random.random()))
        sio.savemat(f'y_ell{i}.mat', {'mydata': y})
        sio.savemat(f'x_ell{i}.mat', {'mydata': x})

        plt.xlim(-x_dia, x_dia)
        plt.ylim(0, z)
        plt.xlabel('r')
        plt.ylabel('Intensity')
        plt.title('ellipse')
        plt.gca().set_aspect('equal')
        # plt.legend()
        plt.grid()
        if i == repeat_:
            plt.savefig("ellipse_energy.svg", dpi=300, format="svg")

    plt.show()

    # This picture is good. Now let's calculate the corresponding integral
    area = np.zeros((repeat_, repeat_))
    # print(area)
    # Cycle 20 times
    for i in range(0, repeat_):
        for j in range(0, repeat_-i):
            x_min = x_dia-i*step_interval-(j+1)*step_interval

            x_max = x_dia-i*step_interval - j*step_interval

            x_values = np.linspace(x_min, x_max, 1000)  # 生成1000个x值

            y_values = z_all[repeat_-i-1] / x_all[repeat_-i-1] * np.sqrt(x_all[repeat_-i-1] ** 2 - x_values ** 2)
            # print(y_values)
            area[i][j] = simps(y_values, x_values)

        area[i] = sorted(area[i])
    print('area: \n', area)
    print('area[0][1]: \n', area[0][1])  #
    # Get the area you need to calculate for each layer
    S_area = np.zeros((repeat_, repeat_))

    for i in range(0, repeat_-1):
        S_area[i] = area[i] - area[i+1]
    S_area[repeat_-1] = area[repeat_-1]
    print('-------------------------------------------------------------------')
    print('S_area: \n', S_area)

    S_area_ = np.transpose(S_area)
    print('S_area_： \n', S_area_)

    # Laser energy consumption
    lambda_ = 1030e-9  # Laser wavelength
    n = 2.5839  # Refractive index of 4H-SiC
    R = 0.19532  # Reflection coefficient of 4H-SiC
    d = 350e-6  # Sample thickness
    k = calculate_k(R, n)
    A = absorption_energy(lambda_, R, d, k)  # The absorbance of energy

    w0 = 2
    layer_n = repeat_
    P_ave = 0.09   # The amount of energy that corresponds to the reduction of the radius
    t = 285e-15  # Laser action time 285 fs
    # In_TTM_bef = GaussGif1d(w0, layer_n, I0, t)  # 100W/cm2 100微米 还需要单脉冲激光的加工时间 10微秒
    f = 1e5
    In_TTM_aft = GaussGif1d(w0, layer_n, P_ave, t, A, f)

    print('In_TTM_aft: \n', In_TTM_aft)
    # In_TTM_aft = np.ones((repeat_, 1))
    # 'repeat_' different parameters are defined to represent the corresponding energy of different layers
    variables = {f'x{i}': sp.symbols(f'x{i}') for i in range(1, repeat_+1)}

    # Convert the contents of the dictionary to a matrix as well
    rows = repeat_
    cols = 1  #

    variables_matrix = np.array(list(variables.values())).reshape(rows, cols)

    print('variables_matrix', variables_matrix)
    # Batch definition of equations
    equations = []
    # alpha = 1e2
    # Solving equations from the outer layer to the inner layer
    x_layer_In = np.linalg.solve(S_area_, In_TTM_aft)*6.241509e18/1e9*8/1000

    print('x_layer_In: \n', x_layer_In)
    with open('output.txt', 'w') as file:
        #

        print('x_layer_In: \n', x_layer_In, file=file)


