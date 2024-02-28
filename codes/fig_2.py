import numpy as np
import matplotlib.pyplot as plt

# Define the function y(n) = n(n+1)(2n+1)/6
def y(n):
    return (n * (n + 1) * (2 * n + 1)) / 6

# Generate a range of n values
n_values = np.arange(0, 10)

# Calculate the theoretical values for y(n)
y_theory = y(n_values)

# Simulate the function using the step function
y_sim = np.cumsum(n_values * (n_values + 1) * (2 * n_values + 1) / 6)

# Plot the simulation versus theory
plt.plot(n_values, y_theory, label='Theory for y_2(n)')
plt.plot(n_values, y_sim, label='Simulation for y_2(n)')

plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('Simulation vs Theory ')
plt.legend()
plt.grid(True)
plt.savefig('y_2(n)')
plt.show()
