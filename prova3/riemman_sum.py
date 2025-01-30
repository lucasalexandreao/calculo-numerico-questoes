from numpy import exp, log

## Soma de Riemann
# A integral de uma função contínua f(x) no intervalo [a, b] pode ser aproximada pela soma de Riemann

def funcion(x):
    return 1 / x * log(x)

def riemman_sum(n, a, b, f):
    """
    n = número de divisões
    [a, b] = intervalo de integração
    f = função a ser integrada
    """
    
    delta = (b-a)/n # largura de cada subintervalo
    
    i = 0
    sum = 0
    
    for i in range(n):
        x = a + i*delta
        sum += f(x) * delta
        
    return sum

def main():
    
    a = exp(1)
    b = exp(1) + 1
    n = 100000
    
    approximate_area = riemman_sum(n, a, b, funcion)
    
    print(f"A área aproximada é {approximate_area}")
    
if __name__ == "__main__":
    main()