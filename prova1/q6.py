from math import ceil, log
from q3 import metodo_bissecao

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
    metodo_bissecao(a, b, tolerancia)
