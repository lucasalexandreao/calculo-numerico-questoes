import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def deriv(y, t, N, beta, gamma, eta, miS, miI):
    '''
    S: Número de indivíduos suscetíveis
    I: Número de indivíduos infectados
    R: Número de indivíduos recuperados
    y: Condições iniciais para o sistema de equações diferenciais
    N: É a representação da população total
    beta: É o coeficiente de transmissão
    gamma: É a taxa de recuperação dos indivíduos infectados
    eta: É a taxa de natalidade dos indivíduos suscetíveis
    miS: É a taxa de mortalidade dos indivíduos suscetíveis
    miI: É a taxa de mortalidade dos indivíduos infectados
    '''

    S, I, R = y
    dSdt = -(beta * S * I) / N + (eta - miS) * S
    dIdt = (beta * S * I) / N - gamma * I - miI * I
    dRdt = gamma * I

    return dSdt, dIdt, dRdt

# Tamanho da População (N=763)
N = 1150000

# Número inicial de infectados e recuperados, I0 and R0.
I0, R0 = 13800, 0

# Número inicial de susceptiveis.
S0 = N - I0 - R0

# Taxa de contato, beta, and mean recovery rate, gamma, (in 1/days).
beta, gamma, eta, miS, miI = 0.13, 0.1, 0.1, 0.1, 0.2

# Discretização do tempo em dias
t = np.linspace(0, 350, 50)

# Condições iniciais para o sistema de equações diferenciais
y0 = S0, I0, R0

# Resolver o modelo SIR de acordo com a discretização do tempo t (em dias).
ret = odeint(deriv, y0, t, args=(N, beta, gamma, eta, miS, miI))
S, I, R = ret.T

# Gráfico do modelo SIR com dinâmica vital
fig = plt.figure(facecolor='w')
ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
plt.title('Modelo SIR com dinâmica vital para 365 dias')
ax.plot(t, S, 'b', alpha=0.5, lw=2, label='Susceptiveis')
ax.plot(t, I, 'r', alpha=0.5, lw=2, label='Infectadas')
ax.plot(t, R, 'g', alpha=0.5, lw=2, label='Recuperadas e com imunidade')
ax.set_xlabel('Tempo(meses)')
ax.set_ylabel('População(1.150.000)')
ax.yaxis.set_tick_params(length=0)
ax.xaxis.set_tick_params(length=0)
ax.grid(visible='True', which='major', c='w', lw=2, ls='-')
legend = ax.legend()
legend.get_frame().set_alpha(0.5)
for spine in ('top', 'right', 'bottom', 'left'):
    ax.spines[spine].set_visible(False)
plt.show()
