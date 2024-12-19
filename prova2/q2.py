# EM PRODUÇÃO
import numpy as np
np.seterr(divide = 'raise')
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


a = [[ 1, -1,  1],
 [ 0, 0, -1],
 [ 0, 0, 6]]

b = [4, -3, 4]

try:
    x = back_substitution(a, b)
    print(x)
except:
    print("Elemento nulo na diagonal principal!\nTente outra matriz.")

