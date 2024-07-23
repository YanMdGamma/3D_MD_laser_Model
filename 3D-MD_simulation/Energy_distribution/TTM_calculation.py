import numpy
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

def TTM_calculation(E_e):
    # 定义参数
    Ce = 75  # 电子比热容，单位为 J/(m·K)
    Cl = 2.5e5  # 4H-SiC 晶格比热容，单位为 J/(kg·K)
    g = 9.8e18  # 电子-晶格耦合系数，单位为 W/(m^3·K)
    # k = 0.0  # 热导率，单位为 W/(m·K)
    dx = 0.01  # 空间步长
    dt = 1e-18  # 时间步长，单位为 s
    L = 1.0  # 空间长度，单位为 m
    T = 1e-15  # 总时间（设置一个较长的时间确保达到平衡），单位为 s

    # 后续简化的话，应该不需要x相关参数
    # 初始化温度分布
    Nx = int(L / dx) + 1
    Nt = int(T / dt) + 1
    Te = np.zeros((Nt, Nx))
    Tl = np.zeros((Nt, Nx))

    # 初始条件
    Te_initial = 300.0  # 初始电子温度（例如，300K）
    Tl_initial = 300.0  # 初始晶格温度（例如，300K）
    Te[0, :] = Te_initial
    Tl[0, :] = Tl_initial

    # 设置电子能量（假设在x=L/2位置有能量）
    E_e = E_e
    Te[0, Nx // 2] += sum(E_e) / Ce  # 确保初始电子温度合理

    # 时间演化
    for n in range(0, Nt - 1):
        for i in range(1, Nx - 1):
            # 电子温度演化方程
            Te_next = Te[n, i] + dt * (- g * (Te[n, i] - Tl[n, i]) / Ce)
            # 晶格温度演化方程
            Tl_next = Tl[n, i] + dt * (g * (Te[n, i] - Tl[n, i]) / Cl)

            # 检查计算结果是否有效
            if np.isnan(Te_next) or np.isnan(Tl_next) or np.isinf(Te_next) or np.isinf(Tl_next):
                raise ValueError(f"Invalid value encountered at step {n}, position {i}: Te={Te_next}, Tl={Tl_next}")

            Te[n + 1, i] = Te_next
            Tl[n + 1, i] = Tl_next

        # 边界条件（假设绝热边界条件）
        Te[n + 1, 0] = Te[n + 1, 1]
        Te[n + 1, -1] = Te[n + 1, -2]
        Tl[n + 1, 0] = Tl[n + 1, 1]
        Tl[n + 1, -1] = Tl[n + 1, -2]

    # 找到平衡时的温度分布
    Te_steady = Te[-1, :]
    Tl_steady = Tl[-1, :]

    # 计算平衡态的晶格温度
    T_eq = Tl[-1, Nx // 2]

    # sio.savemat('Te.mat', {'mydata_Te': Te})
    # sio.savemat('Tl.mat', {'mydata_Tl': Tl})

    Te_final = Te[:, Nx // 2]
    Tl_final = Tl[:, Nx // 2]

    # 插入第一个数值
    Te_final = np.insert(Te_final, 0, Te_initial)
    print("Te_final: ", Te_final)
    Tl_final = np.insert(Tl_final, 0, Tl_initial)
    print("Tl_final: ", Tl_final)

    sio.savemat('Te.mat', {'mydata_Te': Te_final})
    sio.savemat('Tl.mat', {'mydata_Tl': Tl_final})

    # 打印平衡态的晶格温度
    print("电声耦合平衡态的晶格温度:", T_eq)
    # print("电子与声子的平衡态温度：Te: ", Te_steady, " , Tl: ", Tl_steady)

    print("Nx//2: ", Nx//2)

    # 绘制平衡时的温度分布
    y = np.linspace(0, T, Nt + 1) # 要记得加上初始值
    plt.plot(y, Te_final, label='Steady State Electron Temperature (Te)')
    plt.plot(y, Tl_final, label='Steady State Lattice Temperature (Tl)', linestyle='dashed')
    plt.xlabel('Position (x)')
    plt.ylabel('Temperature (K)')
    plt.legend()
    plt.title('Steady State Temperature Distribution in Two-Temperature Model')
    plt.show()

if __name__ == "__main__":
    TTM_calculation([2*1e8])