from euler_method import euler_method, plot
import matplotlib.pyplot as plt

t0 = 1400
tn = 0
def function(t, x):
    g = 9.81
    r = 6371000 # raio da terra
    return -g * ((r ** 2) / ((r + x) ** 2))

def main():

    x, y = euler_method(function, 10, t0, tn, 0)
    plot(x, y, label='Euler', color='blue')

    plt.show()

    print(f'Valor de x: {y[-1]}')

if __name__ == '__main__':
    main()