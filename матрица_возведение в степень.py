# from copy import deepcopy
# n=int(input())
# a=[list(map(int,input().split()))for i in range(n)]
# itog=deepcopy(a)
# m=int(input())
# for l in range(m-1):
#     tekushaj=[[0]*n for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 tekushaj[i][j]+=itog[i][k]*a[k][j]
#     itog=deepcopy(tekushaj)
# for i in itog:
#     print(*i)

# еще решение через функцию
def square_matrix_mult(matrixA, matrixB, size):
    """возведение матрицы в степень"""
    matrixC = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for q in range(size):
                matrixC[i][j] += matrixA[i][q] * matrixB[q][j]
    return matrixC


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
powered_matrix = matrix.copy()

for _ in range(m - 1):
    powered_matrix = square_matrix_mult(matrix, powered_matrix, n)

for row in powered_matrix:
    print(*row)



