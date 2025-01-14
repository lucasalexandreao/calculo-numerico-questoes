import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

T = [(0, 3), (0.5, 1.8616), (1, -0.5571), (1.5, -4.1987), (2, -9.0536)]

# Separa os pontos em coordenadas x e y
x_points, y_points = zip(*T)

# Cria a spline cúbica com os pontos fornecidos
spline = CubicSpline(x_points, y_points)

# Gera valores para o gráfico da função spline
x = np.linspace(0, 10, 500)
y = spline(x)

#print(spline(0.25))


# Cria o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='#FF4500', linewidth=1.5, label="Interpolação Spline Cúbica")
plt.scatter(x_points, y_points, color='blue', s=40, marker='o', label="Pontos originais") # Adiciona os pontos originais
plt.title('Estimativa dos valores gerados pela usina solar')
plt.xlabel('Valores medidos em horas')
plt.ylabel('Energia gerada em Kwh')
plt.grid()
plt.legend()

# Exibe o valor interpolado em x=2
print(f"Valor interpolado em x=0.25: {spline(0.25)}")

# Mostra o gráfico
plt.show()
