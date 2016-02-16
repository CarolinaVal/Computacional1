import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Lee archivo de datos
data = np.loadtxt('datos1.dat')

# Guarda las columnas en los vectores
A = data[:,0]
T = data[:,1]

# Ajuste lineal con parametros m,c
m, c = np.polyfit(A, T, 1)
Aajuste = data[:,0]

# Evaluar xn en el ajuste calculado con los param m,c
Tajuste = np.polyval([m, c], Aajuste)

# Graficar datos y ajuste
plt.plot(data[:,0],data[:,1], 'ro')
plt.plot(Aajuste, Tajuste)

plt.show()