from simpson import simpson
from simpson8 import simpson8
from math import sqrt, pi


# Método de Simpson 1/3

def funcion(x):
    return sqrt(1 - x ** 2)

def main():
    
    # LETRA A
    
    print("Método de Simpson 1/3")
    
    a = -1 # limite inferior
    b = 1 # limite superior
    n = 8 # número de divisões
    
    approximate_area = simpson(n, a, b, funcion)
    
    print(f"A área aproximada é {approximate_area}")

    # LETRA B

    print("Método de Simpson 3/8")
    
    n = 9
    
    approximate_area = simpson8(n, a, b, funcion)
    
    print(f"A área aproximada é {approximate_area}")


if __name__ == "__main__":
    main()