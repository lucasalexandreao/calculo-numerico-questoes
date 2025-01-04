import numpy as np
from q2 import backward_substitution
np.seterr(divide = 'raise')


def gauss(a, b):
    n = len(b)
    for i in range(n):
        for j in range(i + 1, n):
            m = a[j][i] / a[i][i]
            a[j][i] = 0
            for k in range(i + 1, n):
                a[j][k] -= (m * a[i][k])
            b[j] -= (m * b[i])

    return a, b

def main():
    a = np.array([[1,-1,1],[1,0,0],[1,2,4]])
    b = np.array([4,1,-1])


    if np.linalg.det(a):
        try:
            aa, bb = gauss(a, b)
            x = backward_substitution(aa, bb)
            print("Solução do sistema:", x)
        except:
            print("Pivô = 0! Matriz inválida.\nTente com outra matriz.")
    else:
        print("A matriz A possui determinante = 0, logo, é inválida.\nTente com outra matriz.")


if __name__ == '__main__':
    main()



