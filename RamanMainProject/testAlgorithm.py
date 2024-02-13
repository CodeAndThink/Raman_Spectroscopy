import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Generate synthetic data
np.random.seed(42)
x = np.array([1, 2, 3, 4, 5])
true_background_params = [2, 5]  # Coefficients for the true background polynomial
y_true = np.polyval(true_background_params, x) + np.random.normal(0, 2, size=len(x))

# Initial guess for background polynomial (1st degree)
initial_guess = np.polyfit(x, y_true, deg=1)

# Define the background polynomial function
def background_poly(x, a, b):
    return a * x + b

# Iterative fitting
for _ in range(5):  # Repeat for a few iterations
    # Subtract current background estimate
    corrected_data = y_true - background_poly(x, *initial_guess)

    # Refit background polynomial
    fit_params, _ = curve_fit(background_poly, x, corrected_data, p0=initial_guess)

    # Update initial guess for the next iteration
    initial_guess = fit_params

# Final background estimate
final_background = initial_guess

# Subtract final background estimate
background_corrected_data = y_true - background_poly(x, *final_background)

# Plotting
plt.figure(figsize=(12, 6))

# Plot the true data with noise
plt.subplot(2, 2, 1)
plt.scatter(x, y_true, label='True Data with Noise')
plt.legend()

# Plot the initial background estimate
plt.subplot(2, 2, 2)
plt.scatter(x, y_true, label='True Data with Noise')
plt.plot(x, background_poly(x, *initial_guess), color='red', label='Initial Background Estimate')
plt.legend()

# Plot the final background estimate
plt.subplot(2, 2, 3)
plt.scatter(x, y_true, label='True Data with Noise')
plt.plot(x, background_poly(x, *final_background), color='green', label='Final Background Estimate')
plt.legend()

# Plot the background-corrected data
plt.subplot(2, 2, 4)
plt.scatter(x, background_corrected_data, label='Background-Corrected Data')
plt.legend()

plt.tight_layout()
plt.show()
