
import random 

N = int(input("Введите размер матрицы:"))
A = []
print("Матрица А:")
for i in range(N): 
    A.append([0]*N) # добавляем строку с N элементами
    for j in range(N): 
        A[i][j] = random.randint (10,99)
        print ("{:4d}".format(A[i][j]), end = "")
    print() # переход на следующую  строку

#начальные значения максимального и минимального элементов
maxi, maxj = 0, 0 
mini, minj = 0, 0
for i in range(N): 
    for j in range(N):
        if A[i][j] > A[maxi][maxj]:
            maxi, maxj = i, j
        if A[i][j] < A[mini][minj]:
            mini, minj = i, j
            
print("Максимальный элемент A[{0},{1}]={2}".format(maxi,maxj,A[maxi][maxj]))
print("Минимальный элемент A[{0},{1}]={2}".format(mini,minj,A[mini][minj]))
