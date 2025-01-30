import numpy as np
from q2 import backward_substitution
from q3 import gauss


def hilbert(n):
    H = []
    for i in range(1, n+1):
        row = []
        for j in range(1, n+1):
            row.append(1 / (i + j - 1))
        H.append(row)
    return H


def b_generator(n):
    b = []
    for i in range(1, n+1):
        component = 0
        for j in range(1, n+1):
            component += (1 / (i + j - 1))
        b.append(component)
    return b


def main():
    print("b.1 ################")

    for n in range(1, 11):
        print(f"Número de condição de H{n}: {np.linalg.cond(hilbert(n))}")


    print("\nb.2 ################")

    matrices = [hilbert(n) for n in range(3, 11)]
    bs = [b_generator(n) for n in range(3, 11)]
    n = len(matrices)

    for i in range(n):
        matrix, b = gauss(matrices[i], bs[i])
        print(f"Solução do sistema {i+1}: {backward_substitution(matrix, b)}")


if __name__ == '__main__':
    main()
