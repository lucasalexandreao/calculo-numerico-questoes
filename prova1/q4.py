from math import log, ceil
from time import perf_counter


def f(x):
    return (x - 1) ** 2


def falsa_posicao(a, b, epsilon):
    raiz = None
    k = ceil((log(b - a, 10) - log(epsilon, 10)) / log(2, 10))
    iteracoes = 0
    pontos = [a, b]
    pms = []

    if abs(f(a)) < epsilon:
        raiz = a
    elif abs(f(b)) < epsilon:
        raiz = b

    while iteracoes <= k and raiz is None:
        for idx in range(len(pontos) - 1):
            p1 = pontos[idx]
            p2 = pontos[idx + 1]
            pm = (p1 * f(p2) - p2 * f(p1)) / (f(p2) - f(p1))
            if abs(f(pm)) < epsilon:
                raiz = pm
                break
            elif raiz is None:
                if pm not in pontos and pm not in pms:
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
                            pm = (p1 * f(p2) - p2 * f(p1)) / (f(p2) - f(p1))
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

    print("== Método  da falsa posição ==")
    a = float(input("Primeiro número do intervalo: "))
    b = float(input("Segundo número do intervalo: "))
    epsilon = float(input("Epsilon: "))

    try:
        start_time = perf_counter()
        raiz, iteracoes, k = falsa_posicao(a, b, epsilon)
        end_time = perf_counter()

        if raiz is not None:
            print(f"Raiz: {raiz:.5f}\nIterações: {iteracoes}, Limite: {k}\nTempo: {end_time - start_time}")
        elif iteracoes > k:
            print(f"Esta função não tem raiz.\nIterações: {iteracoes}, Limite: {k}\nTempo: {end_time - start_time}")
    except ZeroDivisionError:
        print("Intervalo inválido! Ele gera divisão por zero.")

