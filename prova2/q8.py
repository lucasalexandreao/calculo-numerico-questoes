import numpy as np
from q7 import interpolL, load_data, plot

def main():
    data = 'prova2\q8.csv'
    T = load_data(data)

    p= lambda x: interpolL(x,T) # define o polinomio interpolador p(x)
    print(p(3.1))
    x=np.linspace(0,10,500)

    plot(x, p)


if __name__ == '__main__':
    main()

