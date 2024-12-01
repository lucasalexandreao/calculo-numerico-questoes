from math import log, ceil
from time import perf_counter


def f(x):
    return (x - 1)**2


a = float(input("Primeiro número do intervalo: "))
b = float(input("Segundo número do intervalo: "))
epsilon = 0.0001
raiz = None

k = ceil((log(b-a, 10) - log(epsilon, 10)) / log(2, 10))
iteracoes = 0
pontos = [a, b]
pms = []

start_time = perf_counter()

if abs(f(a)) < epsilon:
    raiz = a
elif abs(f(b)) < epsilon:
    raiz = b

while iteracoes <= k and raiz is None:
    for idx in range(len(pontos) - 1):
        p1 = pontos[idx]
        p2 = pontos[idx + 1]
        pm = (p1 + p2) / 2
        if abs(f(pm)) < epsilon:
            raiz = pm
            break
        elif raiz is None:
            pms.append(pm)
            if f(p1) * f(p2) < 0:
                while abs(p2 - p1) > epsilon:
                    if abs(f(pm)) < epsilon:
                        raiz = pm
                        break
                    elif f(p1) * f(pm) < 0:
                        p2 = pm
                    else:
                        p1 = pm
                    if abs(p2 - p1) > epsilon:
                        pm = (p1 + p2) / 2
                        iteracoes += 1
                raiz = pm
        if raiz is not None:
            break
    iteracoes += 1
    pontos += pms
    pms = []
    pontos.sort()

end_time = perf_counter()

if raiz is not None:
    print(f"Raiz: {raiz:.5f}\nIterações: {iteracoes}, Limite: {k}\nTempo: {end_time - start_time} segundos")
elif iteracoes > k:
    print(f"Esta função não tem raiz neste intervalo\n Iterações: {iteracoes}, Limite: {k}\nTempo: {end_time - start_time}")
