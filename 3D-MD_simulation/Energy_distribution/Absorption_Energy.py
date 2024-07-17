import math

# Calculate extinction coefficient k
def calculate_k(R, n):
    n_squared = n**2
    numerator = n_squared * (R - 1) + 2 * n * (R + 1) + (R - 1)
    denominator = 1 - R
    k = math.sqrt(numerator / denominator)
    print('extinction coefficient: \n', k)
    return k

def absorption_energy(lambda_, R, d, k):

    alpha = float(4*math.pi*k/lambda_)
    print('absorption_coefficient: \n', alpha)

    T = (1 - R)*math.exp(-alpha*d)
    print('Transmittance: \n', T)

    A = 1 - R - T
    print('Absorption: \n', A)
    return A
