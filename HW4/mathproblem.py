import numpy as np

def f(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

a, b = 0, 1 
n = 100  
samples = 100000  

# Riemann Sum Method
dx = (b - a) / n
dy = (b - a) / n
dz = (b - a) / n
x_vals = np.linspace(a, b, n)
y_vals = np.linspace(a, b, n)
z_vals = np.linspace(a, b, n)
riemann_sum = 0

# Summing over each interval in 3D
for x in x_vals:
    for y in y_vals:
        for z in z_vals:
            riemann_sum += f(x, y, z) * dx * dy * dz

# Monte Carlo Method
x_rand = np.random.uniform(a, b, samples)
y_rand = np.random.uniform(a, b, samples)
z_rand = np.random.uniform(a, b, samples)
monte_carlo_sum = (b - a)**3 * np.mean(f(x_rand, y_rand, z_rand))

print("Riemann sum result:", riemann_sum)
print("Monte Carlo result:", monte_carlo_sum)
