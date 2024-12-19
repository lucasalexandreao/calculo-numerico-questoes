import numpy as np

# VERIFICAR DETERMINANTE
# VERIFICAR A11

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

def back_substitution(a, b):
    n = len(b)
    x = np.zeros(n)
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s += a[i][j] * x[j]
        x[i] = (b[i] - s) / a[i][i]
    return x

a = np.array([[1,-1,1],[1,0,0],[1,2,4]])
b = np.array([4,1,-1])
aa, bb = gauss(a, b)
x = back_substitution(aa, bb)
print("Solução do sistema:", x)



