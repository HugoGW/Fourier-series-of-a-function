# Fourier-series-of-a-function

$\textbf{I - Overview}$

This repository contains a Python script that approximates any given function using a Fourier series with a specified number of terms. The script uses the $\textit{numpy}$ and $\textit{matplotlib}$ libraries to perform the numerical calculations and to visualize the approximation process.

$\textbf{II - Fourier Series}$

A Fourier series is a way to represent a function as the sum of simple sine and cosine waves. By increasing the number of terms in the series, the approximation becomes more accurate.

For a function $f(x)$ defined on an interval $[−L,L]$, the Fourier series approximation with $N$ terms is given by:

$$\displaystyle f(x) \approx a_0 + \sum_{n=1}^N a_n \cos⁡ \big(\frac{nπx}{L} \big) + b_n \sin⁡ (\frac{nπx}{L} \big)$$

where the coefficients $a_n$​ and $b_n$​ are calculated as:

$\displaystyle a_n=\frac{1}{L} \int_{−L}^L \cos⁡ \big(\frac{nπx}{L} \big) dx$

$b_n=\frac{1}{L} \int_{−L}^L \sin⁡ \big(\frac{nπx}{L} \big) dx$

$\textbf{III - Code Explanation}$

First, we have to set all Fourier series parameters such as $L$, $n$, $dx$ etc.

    L = np.pi
    n_terms = 200
    dx = 1 / n_terms
    x = np.arange(-L, L, dx)

Then, we define a function to be approximated :

    def f(x):
        return np.tanh(x)

and we calculate the Fourier coefficients and construct the series:

    a_0 = 1 / (2 * L) * np.trapz(f(x), x, dx)
    fourier_series = np.zeros(len(x)) + a_0
    
    fig, ax = plt.subplots(figsize=(8, 8))

where :
- $a_0$ is the zeroth Fourier coefficient, calculated using numerical integration (np.trapz). It represents the average value of the function over one period.
  
- fourier_series: Initializes the Fourier series with the zeroth term. This will be updated iteratively to include more terms.

- fig, ax: These create a figure and an axis for plotting using matplotlib.

and for each $i \in {1,...,n}$ we create a loop that iteratively adds each term of the Fourier series:

    for n in range(1, n_terms):
        # Calculation of mean squared error
        error = np.sqrt(np.trapz(np.abs(np.add(fourier_series, -f(x))) ** 2, x, dx))
    
        # Update plot
        ax.clear()
        ax.plot(x, fourier_series, color='black', label='Fourier Approximation')
        ax.plot(x, f(x), '--', color='blue', label='Initial Function')
        ax.set_title('Approximation of f(x) with {} Fourier terms\nMean Squared Error: {}'.format(n + 1, error))
        ax.grid()
        ax.legend()
    
        plt.draw()
        plt.pause(0.001)
    
        # Compute Fourier coefficients
        a_n = (1 / L) * np.trapz(f(x) * np.cos(np.pi * n * x / L), x, dx)
        b_n = (1 / L) * np.trapz(f(x) * np.sin(np.pi * n * x / L), x, dx)
    
        # Compute the nth Fourier term
        fourier_term = a_n * np.cos(np.pi * n * x / L) + b_n * np.sin(np.pi * n * x / L)
    
        # Update the Fourier series
        fourier_series = np.add(fourier_term, fourier_series)

We add the Mean Squared Error (MSE). This is calculated to measure the difference between the actual function $f(x)$ and the Fourier series approximation at each step.

In the loop, the plot is updated with the current Fourier series approximation and the original function. The title shows the number of terms and the MSE.

Finally, the fourier_term is the $n$th term of the Fourier series that we add in the fourier_series which is the current approximation of the Fourier series.

