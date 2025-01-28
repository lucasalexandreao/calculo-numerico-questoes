from math import sqrt


def function(x):
    return sqrt(1 - x**2)


def boole(n, a, b, function):
    delta = (b - a) / n

    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0

    for i in range(0, n + 1):
        x = a + delta * i
        if i == 0 or i == n:
            sum1 += 7 * function(x)
        elif i % 2 != 0:
            sum2 += 32 * function(x)
        elif i % 4 == 2:
            sum3 += 12 * function(x)
        else:
            sum4 += 14 * function(x)

    return (sum1 + sum2 + sum3 + sum4) * (2 * delta / 45)


def main():
    result = boole(8, -1, 1, function)

    print(f"Regra de Boole Repetida: {result}")


if __name__ == '__main__':
    main()
