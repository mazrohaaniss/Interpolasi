import numpy as np
import matplotlib.pyplot as plt

# Data dari soal
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 20, 22, 15])

def newton_divided_diff(x, y):
    """
    Fungsi untuk menghitung tabel selisih terbagi Newton
    :param x: array dari titik-titik x yang diketahui
    :param y: array dari nilai-nilai y yang diketahui
    :return: tabel selisih terbagi
    """
    n = len(y)
    coef = np.zeros([n, n])
    coef[:, 0] = y
    
    for j in range(1, n):
        for i in range(n - j):
            coef[i][j] = (coef[i + 1][j - 1] - coef[i][j - 1]) / (x[i + j] - x[i])
    
    return coef

def newton_polynomial(coef, x_data, x):
    """
    Fungsi untuk menghitung nilai interpolasi polinomial Newton pada titik x
    :param coef: tabel selisih terbagi
    :param x_data: array dari titik-titik x yang diketahui
    :param x: titik x yang ingin diinterpolasi
    :return: nilai y hasil interpolasi di x
    """
    n = len(x_data) - 1
    p = coef[n]
    for k in range(1, n + 1):
        p = coef[n - k] + (x - x_data[n - k]) * p
    return p

# Menghitung tabel selisih terbagi
coef = newton_divided_diff(x, y)
print("Tabel Selisih Terbagi Newton:")
print(coef)

# Titik yang ingin diinterpolasi
x_interp = np.linspace(min(x), max(x), 500)
y_interp = [newton_polynomial(coef[0], x, xi) for xi in x_interp]

# Plot data asli dan hasil interpolasi
plt.scatter(x, y, color='red', label='Data asli')
plt.plot(x_interp, y_interp, color='blue', label='Interpolasi Polinomial Newton')
plt.xlabel('Tegangan, x (kg/mm²)')
plt.ylabel('Waktu patah, y (jam)')
plt.title('Interpolasi Polinomial Newton untuk Data Tegangan vs Waktu Patah')
plt.legend()
plt.grid(True)
plt.show()
