<<<<<<< HEAD
#we are multiplying matrices (yay!)
import numpy as np

def matmul(A, B):
    
=======
import numpy as np

def print_matrix(M):
    n = M[0].size
    for i in range(n):
        for j in range(n):
            print(M[i][j], "")
        print("\n")
    

def matmul(A, B):
    n = A[0].size
    result = np.zeros((n, n))
    for i in range(n): #rows of A
        #columns of B
        for j in range(n):
            # row of B column
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
    return result

def main():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[2, 3, 4], [5, 6, 7], [8, 9, 10]])
    prod = matmul(A, B)
    print_matrix(prod)

main()
>>>>>>> 3ebaea52fb45f4ad4c4444054764ad49847eb881
