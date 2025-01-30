import numpy as np
from euler_method import euler_method, plot, function
from runge_kutta import runge_kutta
import matplotlib.pyplot as plt


t0 = 1
tn = 0
cd = 0.225 / 1000
g = 9.81
m = 90 / 1000

def f(t, v):
    return g - ((cd / m) * (v ** 2))

def main():
    
    # LETRA A
    x, y = euler_method(function, 10, t0, tn, 0)
    plot(x, y, label='Euler', color='blue')
    
    #LETRA B
    x, y = runge_kutta(function, 10, t0, tn, 0, 4)
    plot(x, y, label='Runge-Kutta 4°', color='orange')

    plt.show()
    
if __name__ == '__main__':
    main()