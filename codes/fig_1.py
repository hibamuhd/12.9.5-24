import numpy as np
import matplotlib.pyplot as plt

# Define the function y(n) = (n(n+1))/2
def y(n):
    return (n * (n + 1)) / 2

# Generate a range of n values
n_values = np.arange(0, 10)

# Calculate the theoretical values for y(n)
y_theory = y(n_values)

# Simulate the function using the step function
y_sim = np.cumsum(n_values)

# Plot the simulation versus theory
plt.plot(n_values, y_theory, label='Theory for y_1(n)', linestyle=':', color='blue')
plt.plot(n_values, y_sim, label='Simulation for y_1(n)', linestyle='-', color='red')

plt.xlabel('n')
plt.ylabel('y(n)')
plt.legend()
plt.grid(True)
plt.savefig('y_1(n).png')
plt.show()
