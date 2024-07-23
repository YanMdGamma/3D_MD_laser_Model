import sympy as sp

def integral_calculation():
    # Defined sign variable
    x = sp.Symbol('x')

    # define function
    f = sp.sin(x) * sp.exp(x)

    # Compute indefinite integral
    indefinite_integral = sp.integrate(f, x)
    print(f"不定积分：{indefinite_integral}")

    #
    definite_integral = sp.integrate(f, (x, 0, sp.pi))
    print(f"定积分（从0到pi）：{definite_integral}")
