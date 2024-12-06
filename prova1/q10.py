import math
import time

def f(x):
    L = 3
    E = 70 * 10 ** 9
    w0 = 15 * 10 ** 3
    I = 52.9 * 10 ** -6
    #form = (w0 * L / (3 * (math.pi ** 4) * E * I))
    #form2 = (48 * L ** 3) * math.cos((math.pi / (2 * L)) * x)
    #form3 = 48 * L ** 3
    #form4 = 3 * (math.pi ** 3) * L * (x ** 2)
    #form5 = - math.pi ** 3 * (x ** 3)
    form1 = (48 * L ** 3) * math.cos((math.pi / (2 * L)) * x)
    form2 = - 48 * L ** 3
    form3 = 3 * (math.pi ** 3) * L * (x ** 2)
    form4 = - math.pi ** 3 * (x ** 3)

    return (w0 * L / (3 * (math.pi ** 4) * E * I)) * (form1 + form2 + form3 + form4)

def h(x):
    return f(x) - 0.009
def derivada(x, epsilon):
    return (h(x + epsilon) - h(x)) / epsilon
def metodo_newton(x0, epsilon, max_iter=100):

    x = x0
    iter_count_newton = 0

    while abs(h(x)) > epsilon and iter_count_newton < max_iter:
        df = derivada(x, epsilon)
        if df == 0:
            raise ValueError("A derivada é zero. O método de Newton pode falhar.")

        x = x - h(x) / df
        iter_count_newton += 1
        print(f"Iteração {iter_count_newton}: x = {x}, h(x) = {f(x)}")

    return x, iter_count_newton

def metodo_secante(x0, x1, epsilon, max_iter=100):
    iter_count_secante = 0

    while abs(h(x1)) > epsilon and iter_count_secante < max_iter:
        if h(x1) == h(x0):
            raise ValueError("Divisão por zero na iteração. Método falhou.")

        # Fórmula do método da secante
        x_new = x1 - h(x1) * (x1 - x0) / (h(x1) - h(x0))

        # Atualizar os pontos
        x0, x1 = x1, x_new
        iter_count_secante += 1
        print(f"Iteração {iter_count_secante}: x = {x1}, f(x) = {f(x1)}")

        if iter_count_secante == max_iter:
            print("Número máximo de iterações atingido.")
            return None

    return x1, iter_count_secante

x0 = 2.0
x0_secante = 3.0
x1_secante = 5.0
epsilon = 1e-6

print("--- Método de Newton ---")
start_newton = time.time()
raiz_newton, iteracao_newton = metodo_newton(x0, epsilon)
end_newton = time.time()
print(f"Raiz: {raiz_newton}")
print(f"Tempo de execução: {end_newton - start_newton}s")
print(f"Quantidade de iterações: {iteracao_newton}")
print()

print("--- Método da Secante ---")
start_secante = time.time()
raiz_secante, iteracao_secante = metodo_secante(x0_secante, x1_secante, epsilon)
end_secante = time.time()
print(f"Raiz: {raiz_secante}")
print(f"Tempo de execução: {end_secante - start_secante}s")
print(f"Quantidade de iterações: {iteracao_secante}")

#print(f(2.35834))
#valor_x = []
#valor_y = []
#intera = []

#for n in range(0,10):
#    for i in range(0,9):
#        j = float(f"{n}.{i}")
#        x, inter = metodo_newton(j,epsilon)
#        if 0 <= x <= 0.009:
#            valor_y.append(x)
#            valor_x.append(j)
#            intera.append(inter)
#        else:
#            os.system("cls")


#os.system("cls")
#print("Os valores de x para y próximo a 9 são:")
#for n in range(len(valor_x)):
#    print(f"Para x = {valor_x[n]}, y = {valor_y[n]}. Quantidade de iterações: {intera[n]}")
