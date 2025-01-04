from math import log, ceil, sqrt
from time import perf_counter
from q3 import metodo_bissecao


def f(x):
    return (x / (1-x)) * sqrt(7/(2 + x)) - 0.04


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

    a = float(input("Primeiro número do intervalo: "))
    b = float(input("Segundo número do intervalo: "))
    epsilon = float(input("Epsilon: "))
    
    print("\n== Método da falsa posição ==")

    try:
        start_time = perf_counter()
        raiz_p, iteracoes_p, k_p = falsa_posicao(a, b, epsilon)
        end_time = perf_counter()

        if raiz_p is not None:
            print(f"Raiz: {raiz_p:.5f}\nIterações: {iteracoes_p}, Limite: {k_p}\nTempo: {end_time - start_time} segundos")
        elif iteracoes_p > k_p:
            print(f"Esta função não tem raiz.\nIterações: {iteracoes_p}, Limite: {k_p}\nTempo: {end_time - start_time} segundos")
    except ZeroDivisionError:
        print("Intervalo inválido! Ele gera divisão por zero.")
        
    print("\n== Método da bisseção ==")
    
    try:
        start_time_bissecao = perf_counter()
        raiz_b, iteracoes_b, k_b = metodo_bissecao(a, b, epsilon)
        end_time_bissecao = perf_counter()

        if raiz_b is not None:
            print(f"Raiz: {raiz_b:.5f}\nIterações: {iteracoes_b}, Limite: {k_b}\nTempo: {end_time_bissecao - start_time_bissecao} segundos")
        elif iteracoes_b > k_b:
            print(f"Esta função não tem raiz.\nIterações: {iteracoes_b}, Limite: {k_b}\nTempo: {end_time_bissecao - start_time_bissecao} segundos")
    except ZeroDivisionError:
        print("Intervalo inválido! Ele gera divisão por zero.")

