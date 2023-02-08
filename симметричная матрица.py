# Проверка мтарицы на симметеричность
n=int(input())
a=[]
for i in range(n):
    a.append(list(map(int,input().split())))
a1=[]
for i in range(n):
    for j in range(n):
        if a[i][j]!=a[j][i]:
            a1.append(False)
            break
        else:
            a1.append(True)
if False in a1:
    print("NO")
else:
    print("YES")
#  еще решение
# n = int(input())
# matrix = [[int(item) for item in input().split()] for _ in range(n)]
# matrix_T = [[matrix[i][j] for i in range(n)] for j in range(n)]
# if (matrix == matrix_T):
#     print("YES")
# else:
#     print("NO")

# еще решение
# В случае симметричной матрици, транспонированная матрица совпадает с оригиналом.
# Для транспонирования используется магия zip. В результате транспонирования
# функция zip создает строки-кортежи вместо строк-список, поэтому чтобы симметричные
# матрицы при сравнении совпали, мы сразу преобразуем каждую строку оригинальной матрицы в кортеж.
# m = [tuple(map(int, input().split())) for _ in range(int(input()))]
# print(('NO', 'YES')[m == [*zip(*m)]])




