"""
Problema: Cálculo do consumo total de CPU ao longo do tempo

Suponha que você está analisando o desempenho de um algoritmo e mediu o uso de CPU (em porcentagem)
em intervalos regulares de tempo (que estão tabelados) para estimar o custo computacional. O uso de CPU ao longo do tempo pode ser modelado pela função
f(t), onde é o tempo em segundos e f(t) é o uso de CPU no instante t.
O objetivo é calcular o consumo total de CPU ao longo do tempo, que pode ser obtido pela integral da função f(t)
no intervalo de tempo [0,8].
"""

from simpson8 import simpson8_table


def main():
    # Tabelas
    time = [0, 1, 2, 3, 4, 5, 6, 7, 8] # Tempo em segundos
    cpu_use = [0, 20, 50, 80, 100, 70, 40, 10, 0] # Uso da CPU em porcentagem

    result = simpson8_table(time, cpu_use)
    print(f"Consumo total da CPU: {result} %·s")


if __name__ == "__main__":
    main()
