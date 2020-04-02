def printMatrix(A): 
    for i in range(len(A)): 
        for j in range(len(A[i])): 
            print ("{:4d}".format(A[i][j]), end = "") 
        print() # переход на следующую строку

print("Введите размер матрицы N и M через пробел:")
N,M = map(int, input().split())
A = []
for i in range(N):
    A.append([0]*M)
    for j in range(M):
        print("A[", i,",",j,"]=", sep = "", end = "")
        A[i][j] = int(input())

printMatrix(A)

