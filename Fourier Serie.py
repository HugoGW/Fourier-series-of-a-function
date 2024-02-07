import numpy as np
import matplotlib.pyplot as plt

# Fourier series parameters
L = np.pi
n_terms = 200
dx = 1 / n_terms
x = np.arange(-L, L, dx)

def f(x):
    return np.tanh(x)

a_0 = 1 / (2 * L) * np.trapz(f(x), x, dx)

fourier_series = np.zeros(len(x)) + a_0

fig, ax = plt.subplots(figsize=(8, 8))

for n in range(1, n_terms):
    
    # Calculation of mean squared error
    error = np.sqrt(np.trapz(np.abs(np.add(fourier_series, -f(x))) ** 2, x, dx))
    
    ax.clear()
    ax.plot(x, fourier_series, color='black', label='Fourier Approximation')
    ax.plot(x, f(x), '--', color='blue', label='Initial Function')
    ax.set_title('Approximation of f(x) with {} Fourier terms\nMean Squared Error: {}'.format(n + 1, error))
    ax.grid()
    ax.legend()

    plt.draw()
    plt.pause(0.001)

    a_n = (1 / L) * np.trapz(f(x) * np.cos(np.pi * n * x / L), x, dx)
    b_n = (1 / L) * np.trapz(f(x) * np.sin(np.pi * n * x / L), x, dx)
    fourier_term = a_n * np.cos(np.pi * n * x / L) + b_n * np.sin(np.pi * n * x / L)
    fourier_series = np.add(fourier_term, fourier_series)

plt.show()
