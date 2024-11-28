def number_or_letter(n):
    if 0 <= n <= 9:
        n = str(n)
    elif 9 < n < 36:
        n += 55
        n = chr(n)
    return n


number = int(input("Insira um número natural qualquer na base 10: "))
base = int(input("Insira um número entre 2 (incluso) e 36 (incluso) para respresentar a base desejada: "))

if (number > 0) and (2 <= base <= 36):
    str_resultado = ""
    num = number
    while num >= base:
        mod = num % base
        mod = number_or_letter(mod)
        str_resultado += mod
        num = num // base
    num = number_or_letter(num)
    str_resultado += num

    print(f"O número {number} na base {base} é: {str_resultado[::-1]}")
else:
    print("Entrada(s) inválida(s)!\nLeia com atenção as instruções de entrada e tente novamente.")
