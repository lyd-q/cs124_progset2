# strassen file - write as own function that takes in a matrix 

#read in the file 



# take in n and crossover value, check if n is less than crossover value
# if n is less than crossover value, run matmul
import numpy as np
import sys

d = int(sys.argv[2])
input_file = sys.argv[3]

A = np.matrix(np.zeros((d, d)))
B = np.matrix(np.zeros((d, d)))
with open(input_file, "r") as file:
    for i in range(d):
        for j in range(d):
            line = file.readline()
            A[i, j] = int(line)
    for i in range(d):
        for j in range(d):
            line = file.readline()
            B[i, j] = int(line)
        

def matmul(A, B):
    n = A[0].size
    result = np.zeros((n, n))
    for i in range(n): #rows of A
        #columns of B
        for j in range(n):
            # row of B column
            for k in range(n):
                result[i, j] += A[i, k] * B[k, j]
    return result

def strassen(M1, M2, n0):
    n = M1.shape[0]
    # if n is larger than the crossover point, we use strassen
    if n >= n0:
         #if n is even, we don't need to pad 
        if n%2 == 0: 

            ret = np.matrix(np.zeros((n, n)))

            #P1 
            X1 = M1[:n/2, :n/2]
            X2 = M2[:n/2, n/2:] - M2[n/2:, n/2:]
            P = strassen(X1, X2, n0)
            
            ret[:n/2, n/2:] += P
            ret[n/2:, n/2:] += P

            #P2 
            X1 = M1[:n/2, :n/2] + M1[:n/2, n/2:]
            X2 = M2[n/2:, n/2:]
            P = strassen(X1, X2, n0) 

            ret[:n/2, :n/2] -= P
            ret[:n/2, n/2:] += P 

            #P3 
            X1 = M1[n/2:, :n/2] + M1[n/2:, n/2:]
            X2 = M2[:n/2, :n/2]
            P = strassen(X1, X2, n0)

            ret[n/2:, :n/2] += P
            ret[n/2:, n/2:] -= P

            #P4 
            X1 = M1[n/2:, n/2:]
            X2 = M2[n/2:, :n/2] - M2[:n/2, :n/2]
            P = strassen(X1, X2, n0)

            ret[:n/2, :n/2] += P
            ret[n/2:, :n/2] += P

            #P5 
            X1 = M1[:n/2, :n/2] + M1[n/2:, n/2:]
            X2 = M2[:n/2, :n/2] + M2[n/2:, n/2:] 
            P = strassen(X1, X2, n0)

            ret[:n/2, :n/2] += P
            ret[n/2:, n/2:] += P

            #P6 
            X1 = M1[:n/2, n/2:] - M1[n/2:, n/2:]
            X2 = M2[n/2:, :n/2] + M2[n/2:, n/2:]
            P = strassen(X1, X2, n0)

            ret[:n/2, :n/2] += P

            #P7 
            X1 = M1[n/2:, :n/2] - M1[:n/2, :n/2]
            X2 = M2[:n/2, :n/2] + M2[:n/2, n/2:]
            P = strassen(X1, X2, n0)

            ret[n/2:, n/2:] += P

            return(ret)
        #if n is odd, we need to pad, and then recursively call again
        else:
            #inefficient padding
            padm1 = np.pad(M1, ((0, 1), (0,1)), mode = 'constant', constant_values = 0)
            padm2 = np.pad(M2, ((0, 1), (0,1)), mode = 'constant', constant_values = 0)
            return strassen(padm1, padm2, n0)[:n, :n]

    else: 
        return matmul(M1, M2)

#test1 = np.matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
#test2 = np.matrix([[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]])
#print(strassen(test1, test2, 3))
# print(test1[:3, :3])


strassen(A, B, 10)