import numpy as np

# Limite à direita
def funcao1(x):
    return (x**4 - 1)

# Limite à esquerda
def funcao2(x):
    return (-x**4 + 1)
    
x0 = 1 #Valor do Limite

n = 100
valor_direita = funcao1(x0 + (1/(10 + n**2)))  # Valor equivalente ao limite lateral pela direita.
valor_esquerda = funcao2(x0 - (1/(10 + n**2)))  # Valor equivalente ao limite lateral pela esquerda.

print("O valor do limite pela direita é:", valor_direita)
print("O valor do limite pela esquerda é:", valor_esquerda)

epsilon = 0.0001
if abs(valor_direita - valor_esquerda) < epsilon:
    print("O limite bilateral é:", valor_direita)
