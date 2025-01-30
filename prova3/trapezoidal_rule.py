from numpy import exp, log

# Regra do Trapézio


def function(x):
    return (97000 * x) / ((-5 * x**2) - 570000)


def trapezoidal_rule(n, a, b, f):
    """
    [a, b] = intervalo de integração
    f = função a ser integrada
    n = número de divisões
    """
    # área do trapézio: (B + b) * h / 2 -> (f(a) + f(b)) * (b - a) / 2
    
    delta = (b-a)/n # altura
    
    sum1 = 0
    
    f_x0 = f(a)
    f_xn = f(b)
    
    for i in range(1, n):
        x = a + i*delta # x1, x2, ..., x(n-1)
        sum1 += f(x)
    
    return (delta / 2) * (f_x0 + 2 * sum1 + f_xn)


def trapezoidal_rule_table(table_x, table_y):
    delta = table_x[1] - table_x[0]
    n = len(table_y)
    total_sum = table_y[0] + table_y[n - 1]
    sum1 = sum(table_y[1: n - 1])
    total_sum += 2 * sum1

    return total_sum * (delta / 2)


def main():
    
    a = 93
    b = 40
    n = 100000
    
    approximate_area = trapezoidal_rule(n, a, b, function)
    
    print(f"A área aproximada é {approximate_area}")


if __name__ == "__main__":
    main()
