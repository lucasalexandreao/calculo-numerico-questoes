import numpy as np
from q2 import backward_substitution
from q3 import gauss

def main():
    first_matrix = {
        "A": np.array([
            [1, -1],
            [1, -1.00001]
        ]),
        "B": np.array([1, 0])
    }

    second_matrix = {
        "A": np.array([
            [1, -1],
            [1, -0.99999]
        ]),
        "B": np.array([1, 0])
    }

    A, B = gauss(first_matrix["A"], first_matrix["B"])
    print("Solução do primeiro sistema: ", backward_substitution(A, B))

    A, B = gauss(second_matrix["A"], second_matrix["B"])
    print("Solução do segundo sistema: ", backward_substitution(A, B))


if __name__ == '__main__':
    main()
