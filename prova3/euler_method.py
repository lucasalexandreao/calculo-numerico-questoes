import matplotlib.pyplot as plt
import numpy as np

# Método de Euler

def function(t, v):
    cd = 0.225 / 1000
    g = 9.81
    m = 90 / 1000
    return g - ((cd / m) * (v ** 2))

def euler_method(f, n, a, b, y0, corretor=False):
    
    '''
    f: função
    n: quantidade de partições
    a: limite inferior
    b: limite superior
    y0: f(x0)
    '''
    
    delta = (b - a) / n 
    
    y = [y0]
    x = np.arange(a, b, delta) # substitui o x = a + i * delta em cada iteração
    
    # equação da reta tangente
    for i in range(x.size - 1):
        y.append(float(y[i] + f(x[i], y[i]) * delta))
        if corretor:
            y[i+1] = float(y[i] + ((f(x[i], y[i]) + f(x[i+1], y[i+1])) / 2) * delta)  
    return x, y


def plot(x, y, label, color):
    plt.plot(x, y, color=color, label=label)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()

def main():
    
    # Exemplo de sala
    x, y = euler_method(function, 10, 0, 2, 0.5)    
    plot(x, y, label='Preditor', color='blue')
    
    x, y = euler_method(function, 10, 0, 2, 0.5, True)
    plot(x, y, label='Corretor', color='red')
    
    plt.show()
       
if __name__ == '__main__':
    main()