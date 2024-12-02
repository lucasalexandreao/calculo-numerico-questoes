import numpy as np
import math

#Limite lateral pela direita/esquerda
def funcao1(x):
    if x == 0:
        return 0 #Caso x seja exatamente 0
    else:
        return x**4 * math.sin(1/x)

x0 = 0 #Valor do Limite
epsilon = 0.0001
n = 100 
valor_direita = funcao1(x0 + (1/(1000 + n**2)))  # Valor equivalente ao limite lateral pela direita.
valor_esquerda = funcao1(x0 - (1/(1000 + n**2)))  # Valor equivalente ao limite lateral pela esquerda
    
print("O valor do limite pela direita é:", valor_direita)
print("O valor do limite pela esquerda é:", valor_esquerda)

if abs(valor_direita - valor_esquerda) < epsilon:
    print("O limite bilateral é:", valor_direita)
