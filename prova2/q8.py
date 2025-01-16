import numpy as np
from q7 import interpolL, load_data, plot
from math import e

def main():
    data = 'q8.csv'
    table = load_data(data)
    T = table[2:5]  # pontos para interpolação
    Tx = [point[0] for point in T]  # valores de x dos pontos

    print("Pontos escolhidos para iterpolação: ", T)

    p= lambda x: interpolL(x,T)  # define o polinomio interpolador p(x)
    result = p(3.1)  #  RESULTADO

    #  LETRA A
    print(f"a) {result}")

    #  LETRA B

    ##  COROLÁRIO 1
    cor1 = 1
    for x in Tx:
        cor1 *= 3.1 - x
    cor1 = abs(cor1)
    M = max([abs(e**x) for x in Tx])
    cor1 *= (M / 6)

    ##  COROLÁRIO 2
    cor2 = ((0.2**3) * M) / 12

    print("b)")
    print("\t# LIMITANTES")
    print(f"\t\tCorolário 1: Erro <= {cor1}")
    print(f"\t\tCorolário 2: Erro < {cor2}")

    x=np.linspace(0,10,500)

    plot(x, p)


if __name__ == '__main__':
    main()

