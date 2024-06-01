import numpy as np
import matplotlib.pyplot as plt

# Data dari soal
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def lagrange_interpolation(x, y, x_point):
    """
    Fungsi untuk menghitung nilai interpolasi Lagrange pada titik x_point
    :param x: array dari titik-titik x yang diketahui
    :param y: array dari nilai-nilai y yang diketahui
    :param x_point: titik x yang ingin diinterpolasi
    :return: nilai y hasil interpolasi di x_point
    """
    n = len(x)
    result = 0
    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (x_point - x[j]) / (x[i] - x[j])
        result += term
    return result

# Titik yang ingin diinterpolasi
x_interp = np.linspace(min(x), max(x), 500)
y_interp = [lagrange_interpolation(x, y, xi) for xi in x_interp]

# Plot data asli dan hasil interpolasi
plt.scatter(x, y, color='red', label='Data asli')
plt.plot(x_interp, y_interp, color='blue', label='Interpolasi Lagrange')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Lagrange untuk Data Tegangan vs Waktu Patah')
plt.legend()
plt.grid(True)
plt.show()
