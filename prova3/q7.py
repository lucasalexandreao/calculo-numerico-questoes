import numpy as np
import matplotlib.pyplot as plt

# Definição dos parâmetros do problema
R = 6.37e6  # Raio da Terra (em metros)
g0 = 9.81  # Aceleração gravitacional na superfície da Terra (m/s^2)
v0 = 1400  # Velocidade inicial do projétil (m/s)
dt = 0.1  # Passo de tempo (em segundos)

# Função que representa a derivada dv/dt
def dvdt(v, x):
    return -g0 * (R**2) / (R + x)**2

# Método de Euler para resolver a equação diferencial
x = 0  # Altura inicial (em metros)
v = v0  # Velocidade inicial (m/s)
t = 0  # Tempo inicial (em segundos)

# Listas para armazenar os valores de tempo, altura e velocidade
t_values = [t]
x_values = [x]
v_values = [v]

# Iteração pelo método de Euler
while v > 0:  # Continuar até que a velocidade seja zero (altura máxima)
    v = v + dvdt(v, x) * dt  # Atualizar velocidade
    x = x + v * dt  # Atualizar altura
    t = t + dt  # Atualizar tempo

    # Armazenar os valores
    t_values.append(t)
    x_values.append(x)
    v_values.append(v)

# Resultados
altura_maxima = max(x_values)
print(f"Altura máxima atingida pelo projétil: {altura_maxima:.2f} m")

# Plot dos resultados
plt.figure(figsize=(10, 6))
plt.plot(t_values, x_values, label="Altura (m)")
plt.xlabel("Tempo (s)")
plt.ylabel("Altura (m)")
plt.title("Altura do Projétil ao Longo do Tempo")
plt.legend()
plt.grid()
plt.show()
