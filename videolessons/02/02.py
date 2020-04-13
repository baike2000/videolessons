import random 

def printMatrix(A): 
    for i in range(len(A)): 
        for j in range(len(A[i])): 
            print ("{:2d}".format(A[i][j]), end = "") 
        print() # переход на следующую строку

def setZero(A):
    for i in range(len(A)): 
        for j in range(len(A[i])): 
            A[i][j] = 0 

N = int(input("Введите размер матрицы:"))
A = []
print("Матрица А:")
for i in range(N): 
    A.append([0]*N) # добавляем строку с N элементами
    for j in range(N): 
        A[i][j] = 0

for i in range(N):
    A[i][i] = i + 1;
print("Главная диагональ:")
printMatrix(A)
setZero(A)
for i in range(N):
    A[i][N-1-i] = i + 1
print("Побочная диагональ:")
printMatrix(A)
setZero(A)
for i in range(N):
    for j in range(i+1):
        A[i][j] = 1
print("Главная диагональ и все элементы которые ниже:")
printMatrix(A)







