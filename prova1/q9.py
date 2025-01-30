import math

def f(x):
    return (math.e ** (39.0744 * x)) * (1 + 39.0744 * x) - (math.e ** 19.5372)
    #return (math.e ** (39.0744 * x - 19.5372)) * (1 + 39.0744 * x) - 1

def derivada(x, epsilon):
    return (f(x + epsilon) - f(x)) / epsilon

def metodo_newton(x0, epsilon):

    x = x0
    iter_count_newton = 0

    while abs(f(x)) > epsilon:
        df = derivada(x, epsilon)
        if df == 0:
            raise ValueError("A derivada é zero. O método de Newton pode falhar.")

        x = x - f(x) / df
        iter_count_newton += 1

    return x, iter_count_newton

if __name__ == "__main__":
    raiz, iteracoes = metodo_newton(2, 0.0001)
    print(f"Vmp: {raiz:.5f} V\nIterações: {iteracoes}")