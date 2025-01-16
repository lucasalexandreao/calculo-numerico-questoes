import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def interpolL(x, T):
    Soma = 0
    for i in range(len(T)):
        produto = 1.0
        for j in range(len(T)):
            if j == i: continue
            produto = produto * (x - T[j][0]) / (T[i][0] - T[j][0])
        Soma = Soma + T[i][1] * produto
    return Soma


def plot(x, p):
    plt.figure(figsize=(5, 5))
    plt.plot(x, p(x), color='#FF4500', marker='', linewidth=1.0)
    plt.title('Estimativa dos valores gerados pela usina solar')
    plt.xlabel('Valores medidos em horas')
    plt.ylabel('Energia gerada em Kwh')
    plt.grid()
    plt.show()


def load_data(path):
    data = pd.read_csv(path, sep=';', names=['x', 'y'])
    data['x'] = data['x'].astype(float)  # converte os numeros de string para float # não pode ter cabeçalho
    data['y'] = data['y'].astype(float)
    return data.values.tolist()  # converte o pd em uma lista de pares ordenados


def main():
    data = 'q7.csv'
    T = load_data(data)

    p = lambda x: interpolL(x, T)  # define o polinomio interpolador p(x)
    print(f"Valor: {p(0.47)}")
    x = np.linspace(0, 10, 500)

    plot(x, p)


if __name__ == '__main__':
    main()


