import time

# Método de Newton e Secante
def f(x):
    return x**3 - 9*x + 3

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

# main
if __name__ == "__main__":
    # Entrada do usuário
    x0 = float(input("Digite o primeiro ponto inicial (x0): "))
    x1 = float(input("Digite o segundo ponto inicial (x1): "))
    epsilon = float(input("Digite o valor da precisão: "))

    # Encontrando a raiz
    print(f'=== Método Newton ===')
    start_newton = time.perf_counter()
    raiz_newton, iter_newton = metodo_newton(x0, epsilon)
    end_newton = time.perf_counter()
    print(f"Raiz: {raiz_newton}")
    print(f'Tempo de execução {end_newton-start_newton}s')
    print()
    print(f'=== Secante ===')
    start_secante = time.perf_counter()
    raiz_secante, iter_secante = metodo_secante(x0, x1, epsilon)
    end_secante = time.perf_counter()
    print(f"Raiz: {raiz_secante}")
    print(f'Tempo de execução {end_secante-start_secante}s')
    print()
    print(f'=== Conclusão ===')

    if end_newton-start_newton < end_secante-start_secante:
        print(f'O método de Newton foi mais rápido.')
    else:
        print(f'O método da Secante foi mais rápido.')