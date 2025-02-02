from numpy import exp, log

# Regra de 1/3 de Simpson


def function(x):
    return x


def simpson(n, a, b, function):
    
    delta = (b-a)/n

    sum1=0
    sum2=0
    sum3=0
    
    for i in range(0,n+1):
        x = a + delta * i
        if (i==0 or i==n):
            sum1 = (sum1 + function(x))
        elif (i%2==0):
            sum2 = (sum2 + 2*function(x))
        else:
            sum3 = (sum3 + 4*function(x))
            
    return (sum1 + sum2 + sum3)*(delta/3)


def simpson_table(table_x, table_y):
    delta = table_x[1] - table_x[0]
    n = len(table_y)
    total_sum = table_y[0] + table_y[n - 1]
    sum1 = 0
    sum2 = 0

    for i in range(1, n - 1):
        if i % 2 == 0:
            sum1 += 2 * table_y[i]
        else:
            sum2 += 4 * table_y[i]
    total_sum += sum1 + sum2

    return total_sum * (delta / 3)


def main():
    
    a = 0
    b = 1
    n = 100000
    
    approximate_area = simpson(n, a, b, function)
    
    print(f"A área aproximada é {approximate_area}")


if __name__ == "__main__":
    main()
