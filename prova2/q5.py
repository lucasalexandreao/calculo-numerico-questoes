import numpy as np

def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=1000):
    """
    Resolve um sistema linear Ax = b usando o método de Gauss-Seidel.

    Parâmetros:
    A: matriz dos coeficientes do sistema (lista de listas)
    b: vetor dos termos independentes (lista)
    x0: vetor inicial (opcional, default é um vetor de zeros)
    tol: tolerância para critério de convergência
    max_iter: número máximo de iterações

    Retorna:
    x: vetor que aproxima a solução do sistema
    iter_count: número de iterações realizadas
    """
    import numpy as np

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


# Função para verificar a diagonal dominante (opcional, mas recomendada)
def is_diagonally_dominant(A):
    """
    Verifica se a matriz A é estritamente diagonal dominante.
    """
    for i in range(len(A)):
        diagonal = abs(A[i][i])
        off_diagonal = sum(abs(A[i][j]) for j in range(len(A)) if j != i)
        if diagonal <= off_diagonal:
            return False
    return True


def sassenfeld(A):
    betas = [1] * len(A)
    for i in range(len(A)):
        diagonal = abs(A[i][i])
        off_diagonal = list(abs(A[i][j]) if j != i else 0 for j in range(len(A)))
        betas[i] = np.dot(off_diagonal, betas)
        if diagonal <= betas[i]:
            return False
    return True


def main():
    # Exemplo de uso
    A = [[4, -1, 0, 0],
         [-1, 4, -1, 0],
         [0, -1, 4, -1],
         [0, 0, -1, 3]]

    b = [15, 10, 10, 10]

    if np.linalg.det(A):
        print("#### CRITÉRIOS DE CONVERGÊNCIA ####")
        rows_criterion = is_diagonally_dominant(A)
        sassenfeld_criterion = sassenfeld(A)
        print(f"Critério das linhas: {"Passou." if rows_criterion else "Não passou."}")
        print(f"Critério de Sassenfeld: {"Passou." if sassenfeld_criterion else "Não passou."}")
        print(f"Ou seja: {"O méotodo irá convergir."if sassenfeld_criterion or rows_criterion else "O método pode não convergir."}\n")

        x, iter_count = gauss_seidel(A, b)
        print("#### SOLUÇÃO ####")
        print(f"Solução aproximada: {x}")
        print(f"Número de iterações: {iter_count}")
    else:
        print("A matriz A possui determinante = 0, logo, é inválida.\nTente com outra matriz.")

if __name__ == '__main__':
    main()
