from math import pi, sqrt
#from q6 import ponto_fixo

# Função para área S
def f(r, h = 20):
    return pi * r * sqrt(r**2 + h**2)

# Função de iteração    
def g(r, h = 20, s = 1200):
    return s / (pi * sqrt(r**2 + h**2))

# Método do Ponto Fixo
def ponto_fixo(a, tol, iter_max):
    c = a # Ponto inicial
    gc = g(c)
    i = 0

    while abs(f(gc)) > tol and i < iter_max - 1:
        c = gc
        gc = g(c)
        i += 1

    print(f"Iterações: {i}")
    print(f"Raio: {gc:.5f}")

# main
if __name__ == "__main__":
    # Valores de entrada
    r = 17 # Raio inicial
    iter_max = 6
    tol = float(input("Digite o valor da tolerância: "))
    
    # Método do ponto fixo
    print("\n== Ponto Fixo ==")
 
    ponto_fixo(r, tol, iter_max)
    
        
        
    