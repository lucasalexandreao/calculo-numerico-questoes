def f(x):
    return x ** 2

def erro_percentual(real, calculado):
    try:
        return (abs(real - calculado) * 100) / real
    except ZeroDivisionError:
        return None


h = float(input("Digite o valor do acréscimo: "))
x = float(input("Digite o ponto para o cálculo da derivada: "))

ordem1_derivada1 = (f(x + h) - f(x)) / h
ordem1_derivada2 = (f(x) - f(x - h)) / h
ordem1_derivada3 = (f(x + h) - f(x - h)) / (2 * h)
ordem1_derivada4 = (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)

ordem2_derivada1 = (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)
ordem2_derivada2 = -(f(x + 2 * h) - 16 * f(x + h) + 30 * f(x) - 16 * f(x - h) + f(x - 2 * h)) / (12 * (h ** 2))
ordem2_derivada3 = (f(x + 2 * h) - 2 * f(x + h) + f(x)) / (h ** 2)
ordem2_derivada4 = (f(x) - 2 * f(x - h) + f(x - 2 * h)) / (h ** 2)

ordem3_derivada1 = (f(x + 2 * h) - 2 * f(x + h) + 2 * f(x - h) - f(x - 2 * h)) / (2 * (h ** 3))
ordem3_derivada2 = (-f(x) + 3 * f(x + h) - 3 * f(x + 2 * h) + f(x + 3 * h)) / (h ** 3)
ordem3_derivada3 = -(-f(x) + 3 * f(x - h) - 3 * f(x - 2 * h) + f(x - 3 * h)) / (h ** 3)
ordem3_derivada4 = -(-f(x - 3 * h) + 8 * f(x - 2 * h) - 13 * f(x - h) + 13 * f(x + h) - 8 * f(x + 2 * h) + f(x + 3 * h)) / (8 * (h ** 3))

valor_esperado1 =float(input("Qual o valor esperado da ordem 1? "))
if (erro_percentual(valor_esperado1, ordem1_derivada1) is None):
    print("No calculo do erro esse valor gera divisão por zero!")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem1_derivada1}")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem1_derivada2}")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem1_derivada3}")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem1_derivada4}")
else:
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem1_derivada1}, Erro: {erro_percentual(valor_esperado1, ordem1_derivada1):.2f} %")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem1_derivada2}, Erro: {erro_percentual(valor_esperado1, ordem1_derivada2):.2f} %")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem1_derivada3}, Erro: {erro_percentual(valor_esperado1, ordem1_derivada3):.2f} %")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem1_derivada4}, Erro: {erro_percentual(valor_esperado1, ordem1_derivada4):.2f} %")

print("\n")

valor_esperado2 =float(input("Qual o valor esperado da ordem 2? "))
if (erro_percentual(valor_esperado2, ordem2_derivada1) is None):
    print("No calculo do erro esse valor gera divisão por zero!")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem2_derivada1}")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem2_derivada2}")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem2_derivada3}")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem2_derivada4}")
else:
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem2_derivada1}, Erro: {erro_percentual(valor_esperado2, ordem2_derivada1):.2f} %")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem2_derivada2}, Erro: {erro_percentual(valor_esperado2, ordem2_derivada2):.2f} %")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem2_derivada3}, Erro: {erro_percentual(valor_esperado2, ordem2_derivada3):.2f} %")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem2_derivada4}, Erro: {erro_percentual(valor_esperado2, ordem2_derivada4):.2f} %")

print("\n")

valor_esperado3 =float(input("Qual o valor esperado da ordem 3? "))
if (erro_percentual(valor_esperado3, ordem3_derivada1) is None):
    print("No calculo do erro esse valor gera divisão por zero!")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem3_derivada1}")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem3_derivada2}")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem3_derivada3}")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem3_derivada4}")
else:
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem3_derivada1}, Erro: {erro_percentual(valor_esperado3, ordem3_derivada1):.2f} %")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem3_derivada2}, Erro: {erro_percentual(valor_esperado3, ordem3_derivada2):.2f} %")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem3_derivada3}, Erro: {erro_percentual(valor_esperado3, ordem3_derivada3):.2f} %")
    print(f"A derivada de primeira ordem da função no ponto desejado é: {ordem3_derivada4}, Erro: {erro_percentual(valor_esperado3, ordem3_derivada4):.2f} %")

