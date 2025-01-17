from math import log, ceil, sqrt
from time import perf_counter

def f(x):
    return (x / (1-x)) * sqrt(7/(2 + x)) - 0.04

# Função para método da bisseção
def metodo_bissecao(a, b, epsilon):
    raiz = None
    iteracoes = 0
    pontos = [a, b]
    pms = []

    k = ceil((log(b-a, 10) - log(epsilon, 10)) / log(2, 10))
    
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

    return raiz, iteracoes, k

 
# main
if __name__ == "__main__":

    print("== Método  da bisseção ==")
    a = float(input("Primeiro número do intervalo: "))
    b = float(input("Segundo número do intervalo: "))
    epsilon = float(input("Valor da precisão: "))

    start_time = perf_counter()
    raiz, iteracoes, k = metodo_bissecao(a, b, epsilon)
    end_time = perf_counter()

    if raiz is not None:
        print(f"Raiz: {raiz:.5f}\nIterações: {iteracoes}, Limite: {k}\nTempo: {end_time - start_time} segundos")
    elif iteracoes > k:
        print(f"Esta função não tem raiz neste intervalo.\nIterações: {iteracoes}, Limite: {k}\nTempo: {end_time - start_time} segundos")