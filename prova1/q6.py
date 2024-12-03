from math import ceil, log

# Função f(x)
def f(x):
    return x * x + x - 6.0

# Função de iteração g(x)
def g(x):
    return 6.0 / (x + 1.0)

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


# Método da bisseção
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

    if raiz is not None:
        print(f"Iterações: {iteracoes}\nRaiz: {raiz:.5f}\nLimite: {k}")
    elif iteracoes > k:
        print(f"Esta função não tem raiz neste intervalo\n Iterações: {iteracoes}, Limite: {k}")

# Valores de entrada
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
tolerancia = float(input("Digite o valor da tolerância: "))

# Método do ponto fixo
print("\n== Ponto Fixo ==")
# Garantir que f(a) e f(b) tenham sinais opostos
while f(a) * f(b) > 0:
    print("\nNão foi possível calcular o valor nesse intervalo.")
    print("Digite um novo intervalo.\n")
    a = float(input("Digite o novo valor de a: "))
    b = float(input("Digite o novo valor de b: "))

ponto_fixo(a, tolerancia)

# Método da bisseção
print("\n== Método  da bisseção ==")

metodo_bissecao(a, b, tolerancia)
