import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
g = 9.81  # aceleração da gravidade (m/s^2)
cd = 0.225  # coeficiente de arrasto (kg/m)
m = 90  # massa do objeto (kg)
y0 = 1000  # altura inicial (m)
v0 = 0  # velocidade inicial (m/s)
t0 = 0  # tempo inicial (s)
h = 0.1  # passo de tempo (s)


# Função para a equação da velocidade
def dvdt(v):
    return g - (cd / m) * v ** 2


# Função para a equação da posição
def dydt(v):
    return -v


# Método de Euler
def euler(y, v, t, h):
    v_new = v + h * dvdt(v)
    y_new = y + h * dydt(v)
    t_new = t + h
    return y_new, v_new, t_new


# Método de Runge-Kutta de 4ª ordem
def runge_kutta(y, v, t, h):
    # Passo 1
    k1_v = h * dvdt(v)
    k1_y = h * dydt(v)

    # Passo 2
    k2_v = h * dvdt(v + k1_v / 2)
    k2_y = h * dydt(v + k1_v / 2)

    # Passo 3
    k3_v = h * dvdt(v + k2_v / 2)
    k3_y = h * dydt(v + k2_v / 2)

    # Passo 4
    k4_v = h * dvdt(v + k3_v)
    k4_y = h * dydt(v + k3_v)

    # Atualização das variáveis
    v_new = v + (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
    y_new = y + (k1_y + 2 * k2_y + 2 * k3_y + k4_y) / 6
    t_new = t + h

    return y_new, v_new, t_new


# Listas para armazenar os valores de tempo, velocidade e altura (Euler)
tempo_euler = []
velocidade_euler = []
altura_euler = []

# Listas para armazenar os valores de tempo, velocidade e altura (Runge-Kutta)
tempo_rk = []
velocidade_rk = []
altura_rk = []

# Iteração até o objeto atingir o chão (Euler)
y_euler, v_euler, t_euler = y0, v0, t0
while y_euler > 0:
    y_euler, v_euler, t_euler = euler(y_euler, v_euler, t_euler, h)
    tempo_euler.append(t_euler)
    velocidade_euler.append(v_euler)
    altura_euler.append(y_euler)

# Iteração até o objeto atingir o chão (Runge-Kutta)
y_rk, v_rk, t_rk = y0, v0, t0
while y_rk > 0:
    y_rk, v_rk, t_rk = runge_kutta(y_rk, v_rk, t_rk, h)
    tempo_rk.append(t_rk)
    velocidade_rk.append(v_rk)
    altura_rk.append(y_rk)

# Resultados finais
print("Resultados com o método de Euler:")
print(f"Tempo de queda: {t_euler:.2f} s")
print(f"Velocidade: {v_euler:.2f} m/s")

print("\nResultados com o método de Runge-Kutta:")
print(f"Tempo de queda: {t_rk:.2f} s")
print(f"Velocidade: {v_rk:.2f} m/s")

# Plotando os gráficos
plt.figure(figsize=(14, 6))

# Gráfico da velocidade em função do tempo
plt.subplot(1, 2, 1)
plt.plot(tempo_euler, velocidade_euler, label='Euler - Velocidade (m/s)', color='blue', linestyle='--')
plt.plot(tempo_rk, velocidade_rk, label='Runge-Kutta - Velocidade (m/s)', color='red')
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Velocidade em função do tempo')
plt.grid()
plt.legend()

# Gráfico da altura em função do tempo
plt.subplot(1, 2, 2)
plt.plot(tempo_euler, altura_euler, label='Euler - Altura (m)', color='blue', linestyle='--')
plt.plot(tempo_rk, altura_rk, label='Runge-Kutta - Altura (m)', color='red')
plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')
plt.title('Altura em função do tempo')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

