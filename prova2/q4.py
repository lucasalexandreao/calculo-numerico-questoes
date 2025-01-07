import numpy as np
from q5 import is_diagonally_dominant


def stop_test(x, x_new, n, tol):
    distance = max(abs(x_new[i] - x[i]) for i in range(n))
    relative_distance = distance / (max(map(abs, x_new)))

    if relative_distance < tol:
        return True
    return False


def gauss_jacobi(A, b, x0, tol=1e-6, max_iter=1000):
    """
    Resolve o sistema linear Ax = b utilizando o método iterativo de Gauss-Jacobi.

    Parâmetros:
    A: np.ndarray
    Matriz dos coeficientes do sistema.
    b: np.ndarray
    Vetor do lado direito do sistema.
    x0: np.ndarray
    Vetor inicial.
    tol: float, opcional
    Tolerância para critério de parada (default é 1e-6).
    max_iter: int, opcional
    Número máximo de iterações (default é 100).

    Retorna:
    x: np.ndarray
    Vetor que aproxima a solução do sistema.
    iter_count: int
    Número de iterações realizadas.
    """

    n = len(b)
    x = x0.copy()
    x_new = np.zeros_like(x, dtype=float)

    for k in range(max_iter):
        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - sigma) / A[i, i]

        #if np.linalg.norm(x_new - x, ord=np.inf) < tol:
        if stop_test(x, x_new, n, tol):
            return x_new, k + 1

        x = x_new.copy()

    raise ValueError("O método de Gauss-Jacobi não convergiu dentro do número máximo de iterações.")

def main():
# Exemplo de uso:
    A = np.array([[10, 2, 1],
                  [1, 5, 1],
                  [2, 3, 10]])

    b = np.array([7, -8, 6])

    x0 = np.zeros_like(b, dtype=float)

    if np.linalg.det(A):
        print("#### CRITÉRIOS DE CONVERGÊNCIA ####")
        print(f"Critério das linhas: {"Passou! O método irá convergir." if is_diagonally_dominant(A) else "Não passou! o método pode não convergir."}\n")

        solution, iterations = gauss_jacobi(A, b, x0)
        print("#### SOLUÇÃO ####")
        print("Solução aproximada:", solution)
        print("Número de iterações:", iterations)
    else:
        print("A matriz A possui determinante = 0, logo, é inválida.\nTente com outra matriz.")

if __name__ == '__main__':
    main()

