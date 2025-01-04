import numpy as np
from q2 import backward_substitution


def lu_decomposition(A):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for j in range(n):
        U[j][j] = 1

        for i in range(j, n):
            L[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(j))

        for i in range(j + 1, n):
            U[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / L[j][j]

    return L, U


def forward_substitution(L, b):
    n = len(b)
    y = np.zeros_like(b, dtype=float)

    for i in range(n):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]

    return y


def solve_linear_system(A, B):
    L, U = lu_decomposition(A)
    y = forward_substitution(L, B)
    x = backward_substitution(U, y)

    return x


def main():
    A = [[1, -1, 1], [1, 0, 0], [1, 2, 4]]
    B = [4, 1, -1]

    if np.linalg.det(A):
        x = solve_linear_system(A, B)
        print("Solução do sistema:", x)
    else:
        print("A matriz A possui determinante = 0, logo, é inválida.\nTente com outra matriz.")


if __name__ == '__main__':
    main()
