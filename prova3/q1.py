from simpson8 import simpson8_table
from trapezoidal_rule import trapezoidal_rule_table

def main():
    table_x = [0, 80, 160, 240, 320, 400, 480, 560, 640, 720, 800, 880, 960, 1040, 1120, 1200]
    table_y_positive = [0, 0, 0, 0, 0, 480, 480, 480, 255, 230, 220, 205, 200, 220, 200, 0]
    table_y_negative = [0, -90, -160, -310, -330, -245, -250, -330, -480, -600, -640, -650, -415, -365, -250, -240]

    # Método do Ponto Central
    trapezoidal_area = trapezoidal_rule_table(table_x, table_y_positive) + abs(trapezoidal_rule_table(table_x, table_y_negative))

    # Método de Simpson 3/8 composto
    simpson8_area = simpson8_table(table_x, table_y_positive) + abs(simpson8_table(table_x, table_y_negative))

    print(f"Método do ponto central: {trapezoidal_area} km²")
    print(f"Método de Simpson 3/8 composto: {simpson8_area} km²")


if __name__ == "__main__":
    main()