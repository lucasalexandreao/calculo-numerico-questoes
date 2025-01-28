import numpy as np
np.seterr(invalid='raise', divide='raise')


def is_diagonally_dominant(A):
    for i in range(len(A)):
        diagonal = abs(A[i][i])
        off_diagonal = sum(abs(A[i][j]) for j in range(len(A)) if j != i)
        if diagonal <= off_diagonal:
            return False
    return True


def zero_in_diagonal(A):
    n = len(A)
    for i in range(n):
        if A[i][i] == 0:
            return True
    return False


def equal_values(B):
    return len(set(B)) == 1


def is_appropiate_solution(A, x, b):
    return np.allclose(np.dot(A, x), b)


def stop_test(x, x_new, n, tol):
    distance = max(abs(x_new[i] - x[i]) for i in range(n))
    relative_distance = distance / (max(map(abs, x_new)))

    if relative_distance < tol:
        return True
    return False


def gauss_jacobi(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x, dtype=float)

    for k in range(max_iter):
        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - sigma) / A[i, i]

        if stop_test(x, x_new, n, tol):
            return x_new, k + 1

        x = x_new.copy()

    raise ValueError("O método de Gauss-Jacobi não convergiu dentro do número máximo de iterações.")


def main():
    # Exemplo de uso:
    A = np.array([[1, 0.5, -0.1, 0.1], [0.2, 1, -0.2, -0.1], [-0.1, -0.2, 1, 0.2], [0.1, 0.3, 0.2, 1]])
    b = np.array([0.2, -2.6, 1, -2.5])

    #A = np.array([[1, 3, 1], [5, 2, 2], [0, 6, 8]])
    #b = np.array([-2, 3, -6])

    #A = np.array([[5, 2, 2], [1, 3, 1], [0, 6, 8]])
    #b = np.array([3, -2, -6])

    x0 = np.zeros_like(b, dtype=float)

    if not np.linalg.det(A):
        print("A matriz A possui determinante = 0, logo, é inválida.\nTente com outra matriz.")
    elif zero_in_diagonal(A):
        print("A matriz possui zero na diagonal principal, o método não convergirá!")
    else:
        print("#### CRITÉRIOS DE CONVERGÊNCIA ####")
        print(f"Valores do vetor b: {"Todos os valores são iguais, um indício de que TALVEZ não convirja" if equal_values(b) else "Há ao menos um valor distinto dos outros."}")
        print(f"Critério das linhas: {"Passou! O método irá convergir." if is_diagonally_dominant(A) else "Não passou! o método pode não convergir."}\n")

        print("#### SOLUÇÃO ####")

        solution, iterations = gauss_jacobi(A, b, x0)

        if is_appropiate_solution(A, solution, b):
            print("Solução aproximada:", solution)
            print("Número de iterações:", iterations)
        else:
            print("A solução encontrada não é apropriada!")



if __name__ == '__main__':
    main()

