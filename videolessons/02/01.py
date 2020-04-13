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
for i in range(N): 
    for j in range(N):
        if (j > i):
            A[i][j] = 0
        else:
            A[i][j] -= 1

print("Результат:")
for i in range(N): 
    for j in range(N): 
        print ("{:4d}".format(A[i][j]), end = "")
    print() # переход на следующую  строку
           
