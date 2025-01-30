import numpy as np
import matplotlib.pyplot as plt
from euler_method import euler_method, plot, function

def runge_kutta(f, n, a, b, y1, order):
    
    delta = (b - a) / n
    
    x = np.arange(a,b,delta)
    y = []
    
    for i in x:
        y.append(y1)
        if order == 2:
            k1 = f(i,y1)
            k2 = f(i+delta,y1+delta*k1)
            y1 = y1 + 0.5*delta*(k1+k2)

        if order == 4:
            k1 = f(i,y1)
            k2 = f( i+ 0.5*delta,y1 + 0.5*delta*k1)
            k3 = f(i+ 0.5*delta, y1 + 0.5*delta*k2 )
            k4 = f(i+ delta, y1 + k3*delta)
            y1 = (y1 + (1/6)*delta*(k1+2*k2+2*k3+k4))
    return x, y

def main():
    x, y = runge_kutta(function, 10, 0, 2, 0.5, 2)
    plot(x, y, label='Runge-Kutta 2°', color='yellow')
    
    x, y = runge_kutta(function, 10, 0, 2, 0.5, 4)
    plot(x, y, label='Runge-Kutta 4°', color='orange')
    
    x, y = euler_method(function, 10, 0, 2, 0.5)    
    plot(x, y, label='Preditor', color='blue')
    
    x, y = euler_method(function, 10, 0, 2, 0.5, True)
    plot(x, y, label='Corretor', color='red')
    
    plt.show()

if __name__ == '__main__':
    main()
