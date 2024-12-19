# EM PRODUÇÃO

'''
import numpy as np

def lu_decomposition(A):
    """Realiza a decomposição LU da matriz A."""
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        L[i][i] = 1 # Diagonal da L é 1

    for j in range(i, n):
        U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))

    for j in range(i + 1, n):
        L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

def forward_substitution(L, b):
    """Resolve Ly = b usando substituição direta."""
    n = len(b)
    y = np.zeros_like(b)

    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))

    return y

def backward_substitution(a, b):
    n = len(b)
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += a[i][j] * x[j]
        x[i] = (b[i] - s) / a[i][i]
    return x

def solve_linear_system(A, B):
    """Resolve o sistema linear Ax = B usando a decomposição LU."""
    L, U = lu_decomposition(A)
    y = forward_substitution(L, B)
    x = backward_substitution(U, y)
    return x

# Exemplo de uso
A = np.array([[1, -1, 1],
[1, 0, 0],
[1, 2, 4]], dtype=float)

B = np.array([4, 1, -1], dtype=float)

x = solve_linear_system(A, B)
print("Solução x:", x)
'''
