from math import ceil, log
from q3 import metodo_bissecao

# Função f(x)
def f(x):
    return x * x + x - 6.0

# Função de iteração g(x)
def g(x):
    return 6.0 / (x + 1.0)


def metodo_bissecao(a, b, epsilon):
    raiz = None
    iteracoes = 0
    pontos = [a, b]
    pms = []

    k = ceil((log(b - a, 10) - log(epsilon, 10)) / log(2, 10))

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


# Método do Ponto Fixo
def ponto_fixo(a, tol):
    c = a # Ponto inicial
    gc = g(c)
    i = 0

    while abs(f(gc)) > tol:
        c = gc
        gc = g(c)
        i += 1

    print(f"Iterações: {i}")
    print(f"Raiz aproximada: {gc:.5f}")

# main
if __name__ == "__main__":
    # Valores de entrada
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    tolerancia = float(input("Digite o valor da tolerância: "))
    
    # Garantir que f(a) e f(b) tenham sinais opostos
    while f(a) * f(b) > 0:
        print("\nNão foi possível calcular o valor nesse intervalo.")
        print("Digite um novo intervalo.\n")
        a = float(input("Digite o novo valor de a: "))
        b = float(input("Digite o novo valor de b: "))
    
    # Método do ponto fixo
    print("\n== Ponto Fixo ==")
    ponto_fixo(a, tolerancia)


    # Método da bisseção
    print("\n== Método  da bisseção ==")
    raiz_bisseccao, iteracoes_bisseccao, k = metodo_bissecao(a, b, tolerancia)
    print(f"Iterações: {iteracoes_bisseccao}")
    print(f"Raiz aproximada: {raiz_bisseccao:.5f}")
