def printMatrix(A): 
    for i in range(len(A)): 
        for j in range(len(A[i])): 
            print ("{:4d}".format(A[i][j]), end = "") 
        print() # переход на следующую строку

A = [[-1, 0, 1], 
     [-1, 0, 1], 
     [0, 1, -1]]

printMatrix(A)

