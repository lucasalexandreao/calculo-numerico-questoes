import numpy as np
np.seterr(invalid='raise', divide='raise')


def is_diagonally_dominant(A):
    for i in range(len(A)):
        diagonal = abs(A[i][i])
        off_diagonal = sum(abs(A[i][j]) for j in range(len(A)) if j != i)
        if diagonal <= off_diagonal:
            return False
    return True


def sassenfeld(A):
    n = len(A)
    betas = [1] * n
    for i in range(n):
        diagonal = abs(A[i][i])
        off_diagonal = list(abs(A[i][j]) if j != i else 0 for j in range(n))
        betas[i] = np.dot(off_diagonal, betas) / diagonal
        if betas[i] >= 1:
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


def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=1000):
    n = len(b)
    if x0 is None:
        x = [0.0] * n  # Vetor inicial padrão
    else:
        x = x0.copy()

    for k in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sigma) / A[i][i]

        # Critério de convergência (norma relativa)
        norm_diff = np.linalg.norm(np.array(x) - np.array(x_old), ord=np.inf)
        norm_x = np.linalg.norm(np.array(x), ord=np.inf)
        if norm_diff / max(norm_x, 1) < tol:
            return x, k + 1  # Retorna solução e número de iterações

    raise ValueError("O método de Gauss-Seidel não convergiu após o número máximo de iterações.")


def main():
    # Exemplo de uso
    A = [[1, 0.5, -0.1, 0.1], [0.2, 1, -0.2, -0.1], [-0.1, -0.2, 1, 0.2], [0.1, 0.3, 0.2, 1]]
    b = [0.2, -2.6, 1, -2.5]

    #A = [[2, 1, 3], [0, -1, 1], [1, 0, 3]]
    #b = [9, 1, 3]

    #A = [[3, 0, 1], [1, -1, 0], [3, 1, 2]]
    #b = [3, 1, 9]

    #A = [[1, 3, 1], [5, 2, 2], [0, 6, 8]]
    #b = [-2, 3, -6]

    #A = [[5, 2, 2], [1, 3, 1], [0, 6, 8]]
    #b = [3, -2, -6]


    if not np.linalg.det(A):
        print("A matriz A possui determinante = 0, logo, é inválida.\nTente com outra matriz.")
    elif zero_in_diagonal(A):
        print("A matriz possui zero na diagonal principal, o método não convergirá!")
    else:
        print("#### CRITÉRIOS DE CONVERGÊNCIA ####")
        rows_criterion = is_diagonally_dominant(A)
        sassenfeld_criterion = sassenfeld(A)
        print(f"Valores do vetor b: {"Todos os valores são iguais, um indício de que TALVEZ não convirja" if equal_values(b) else "Há ao menos um valor distinto dos outros."}")
        print(f"Critério das linhas: {"Passou." if rows_criterion else "Não passou."}")
        print(f"Critério de Sassenfeld: {"Passou." if sassenfeld_criterion else "Não passou."}")
        print(f"Ou seja: {"O método irá convergir."if sassenfeld_criterion or rows_criterion else "O método pode não convergir."}\n")

        print("#### SOLUÇÃO ####")
        try:
            x, iter_count = gauss_seidel(A, b)

            if is_appropiate_solution(A, x, b):
                print(f"Solução aproximada: {x}")
                print(f"Número de iterações: {iter_count}")
            else:
                print("A solução encontrada não é apropriada!")
        except:
            print("O método não convergiu.")


if __name__ == '__main__':
    main()
