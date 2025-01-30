from simpson8 import simpson8_table


def central_point_table(table_x, table_y):
    delta = table_x[1] - table_x[0]
    n = len(table_y)
    total_sum = 0

    for i in range(n - 1):
        central = (table_y[i] + table_y[i + 1]) / 2
        total_sum += central * delta

    return total_sum


def main():
    table_x = [0, 80, 160, 240, 320, 400, 480, 560, 640, 720, 800, 880, 960, 1040, 1120, 1200]
    table_y_positive = [0, 0, 0, 0, 0, 480, 480, 480, 255, 230, 220, 205, 200, 220, 200, 0]
    table_y_negative = [0, -90, -160, -310, -330, -245, -250, -330, -480, -600, -640, -650, -415, -365, -250, -240]

    # Método do Ponto Central
    central_point_area = central_point_table(table_x, table_y_positive) + abs(central_point_table(table_x, table_y_negative))

    # Método de Simpson 3/8 composto
    simpson8_area = simpson8_table(table_x, table_y_positive) + abs(simpson8_table(table_x, table_y_negative))

    print(f"Método do ponto central: {central_point_area} km²")
    print(f"Método de Simpson 3/8 composto: {simpson8_area} km²")


if __name__ == "__main__":
    main()
