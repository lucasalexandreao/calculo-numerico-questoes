import numpy as np


def newton_polynomial(x, y, value, llimit=0, ulimit=0):
    if ulimit == 0:
        ulimit = len(x) - 1

    dg = ulimit - llimit + 2
    n = len(x)
    p = np.zeros([n, n+1])

    #  primeiras duas colunas da tabela de diferenças divididas
    for i in range(n):
        p[i, 0] = x[i]
        p[i, 1] = y[i]

    #  tabela de diferenças divididas
    for i in range(2,n+1):
        for j in range(n+1-i):
            p[j, i]=(p[j+1, i-1] - p[j, i-1])/(x[j + i - 1] - x[j])  # Tree Table

    x = x[llimit:ulimit+1]
    y = y[llimit:ulimit+1]
    b = p[llimit][1:dg]  #  coeficientes do polinômio

    lst = []  # (x-x0), (x-x0)(x-x1), (x-x0)(x-x1)(x-x2), ...
    t = 1
    for i in range(len(x)):
        t *= (value-x[i])
        lst.append(t)

    f = b[0]
    for k in range(1,len(b)):
        f += b[k] * lst[k-1]

    return p, f


"""
def max_in_table(table, n):
    table = [row[1:n+2] for row in table]
    most = 0
    for i in range(len(table[0])):
        for j in range(len(table[0])):
            abs_value = abs(table[i][j])
            if abs_value > most:
                most = abs_value
    return most
"""


def max_in_table(table, n):
    most = 0
    for i in table:
        abs_value = abs(i[n+1])
        if abs_value > most:
            most = abs_value
    return most


def error_estimate(xs, x,  M):
    mult = 1
    for i in xs:
        mult *= x - i
    mult = abs(mult) * abs(M)
    return mult

def main():
    x = np.array([1, 2, 3, 5, 6], float)
    y = np.array([0.75, 0.64, 0.24, 2.94, 0.37], float)

    #  LETRA A
    table_a, solution_a = newton_polynomial(x, y, 4, 1, 3)
    print(f"a) Estimativa do valor: {solution_a:.2f}")

    #  LETRA B
    M = max_in_table(table_a, 3)
    error_margin = error_estimate(x[1:4], 4, M)
    print(f"b) Estimativa do erro: {error_margin:.2f}")

    #  LETRA C
    max_half_yearly_estimate = solution_a + sum(y) + error_margin
    answer_c = "não" if max_half_yearly_estimate > 6 else "sim,"
    print(f"c) O valor máximo estimado é {max_half_yearly_estimate:.2f}%, logo, {answer_c} podemos garantir que a inflação semestral foi menor que 6%.")

    # LETRA D
    table_d, solution_d = newton_polynomial(x, y, 7, 2, 4)
    print(f"a) Estimativa do valor: {solution_d:.2f}")


if __name__ == '__main__':
    main()

