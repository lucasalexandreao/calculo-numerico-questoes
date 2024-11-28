def f(x):
    return (x ** 2)


h = float(input("Digite o valor do acréscimo: "))
x = float(input("Digite o ponto para o cálculo da derivada: "))

ordem1_derivada1 = (f(x + h) - f(x)) / h
ordem1_derivada2 = (f(x) - f(x - h)) / h
ordem1_derivada3 = (f(x + h) - f(x - h)) / (2 * h)
ordem1_derivada4 = (-f(x + 2 * h) + 8 * f(x + h) - 8 * f(x - h) + f(x - 2 * h)) / (12 * h)

derivada1_ordem2 = (f(x + h) - 2 * f(x) + f(x - h)) / (h ** 2)
derivada2_ordem2 = -(f(x + 2 * h) - 16 * f(x + h) + 30 * f(x) - 16 * f(x - h) + f(x - 2 * h)) / (12 * (h ** 2))
ordem2_derivada3 = (f(x + 2 * h) - 2 * f(x + h) + f(x)) / (h ** 2)
ordem2_derivada4 = (f(x) - 2 * f(x - h) + f(x - 2 * h)) / (h ** 2)

ordem3_derivada1 = (f(x + 2 * h) - 2 * f(x + h) + 2 * f(x - h) - f(x - 2 * h)) / (2 * (h ** 3))
ordem3_derivada2 = (-f(x) + 3 * f(x + h) - 3 * f(x + 2 * h) + f(x + 3 * h)) / (h ** 3)
ordem3_derivada3 = (-f(x) + 3 * f(x - h) - 3 * f(x - 2 * h) + f(x - 3 * h)) / (h ** 3)
ordem3_derivada4 = (-f(x - 3 * h) + 8 * f(x - 2 * h) - 13 * f(x - h) + 13 * f(x + h) - 8 * f(x + 2 * h) + f(x + 3 * h)) / (8 * (h ** 3))

print("A derivada de primeira ordem da função no ponto desejado é:", ordem1_derivada1)
print("A derivada de primeira ordem da função no ponto desejado é:", ordem1_derivada2)
print("A derivada de primeira ordem da função no ponto desejado é:", ordem1_derivada3)
print("A derivada de primeira ordem da função no ponto desejado é:", ordem1_derivada4)
print("\n")
print("A derivada de segunda ordem da função no ponto desejado é:", derivada1_ordem2)
print("A derivada de segunda ordem da função no ponto desejado é:", derivada2_ordem2)
print("A derivada de segunda ordem da função no ponto desejado é:", ordem2_derivada3)
print("A derivada de segunda ordem da função no ponto desejado é:", ordem2_derivada4)
print("\n")
print("A derivada de terceira ordem da função no ponto desejado é:", ordem3_derivada1)
print("A derivada de terceira ordem da função no ponto desejado é:", ordem3_derivada2)
print("A derivada de terceira ordem da função no ponto desejado é:", ordem3_derivada3)
print("A derivada de terceira ordem da função no ponto desejado é:", ordem3_derivada4)

