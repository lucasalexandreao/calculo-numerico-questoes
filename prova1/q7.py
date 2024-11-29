import time
import matplotlib.pyplot as plt
import numpy as np

# Método de Newton e Secante
def f(x):
    return x**2 - 2*x + 1

def derivada(x, epsilon):
    return (f(x + epsilon) - f(x)) / epsilon

def metodo_newton(x0, epsilon, max_iter=100):

    x = x0
    iter_count_newton = 0

    while abs(f(x)) > epsilon and iter_count_newton < max_iter:
        df = derivada(x, epsilon)
        if df == 0:
            raise ValueError("A derivada é zero. O método de Newton pode falhar.")

        x = x - f(x) / df
        iter_count_newton += 1
        print(f"Iteração {iter_count_newton}: x = {x}, f(x) = {f(x)}")

    return x, iter_count_newton

def metodo_secante(x0, x1, epsilon, max_iter=100):

    iter_count_secante = 0

    while abs(f(x1)) > epsilon and iter_count_secante < max_iter:
        if f(x1) == f(x0):
            raise ValueError("Divisão por zero na iteração. Método falhou.")

        # Fórmula do método da secante
        x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

        # Atualizar os pontos
        x0, x1 = x1, x_new
        iter_count_secante += 1
        print(f"Iteração {iter_count_secante}: x = {x1}, f(x) = {f(x1)}")

        if iter_count_secante == max_iter:
            print("Número máximo de iterações atingido.")
            return None

    return x1, iter_count_secante

# Plotando comparação das iterações dos métodos de Newton e Secante em função do tempo
def plotar_iteracoes(x0, x1, epsilon):
    iteracoes_newton = []
    iteracoes_secante = []
    tempo_newton = []
    tempo_secante = []

    for i in range(1, 100):
        start_newton = time.time()
        metodo_newton(x0, epsilon, i)
        end_newton = time.time()
        tempo_newton.append(end_newton - start_newton)
        iteracoes_newton.append(i)

        start_secante = time.time()
        metodo_secante(x0, x1, epsilon, i)
        end_secante = time.time()
        tempo_secante.append(end_secante - start_secante)
        iteracoes_secante.append(i)

    plt.plot(iteracoes_newton, tempo_newton, label="Newton")
    plt.plot(iteracoes_secante, tempo_secante, label="Secante")
    plt.xlabel("Iterações")
    plt.ylabel("Tempo (s)")
    plt.title("Iterações x Tempo")
    plt.legend()
    plt.show()
    
# Entrada do usuário
x0 = float(input("Digite o primeiro ponto inicial (x0): "))
x1 = float(input("Digite o segundo ponto inicial (x1): "))
epsilon = float(input("Digite o valor da precisão: "))

# Encontrando a raiz
print(f'=== Método Newton ===')
start_newton = time.time()
raiz_newton, iter_newton = metodo_newton(x0, epsilon)
end_newton = time.time()
print(f"Raiz: {raiz_newton}")
print(f'Tempo de execução {end_newton-start_newton}s')
print()
print(f'=== Secante ===')
start_secante = time.time()
raiz_secante, iter_secante = metodo_secante(x0, x1, epsilon)
end_secante = time.time()
print(f"Raiz: {raiz_secante}")
print(f'Tempo de execução {end_secante-start_secante}s')
print()
print(f'=== Conclusão ===')

if end_newton-start_newton < end_secante-start_secante:
    print(f'O método de Newton foi mais rápido.')
else:
    print(f'O método da Secante foi mais rápido.')
    
plotar_iteracoes(x0, x1, epsilon)