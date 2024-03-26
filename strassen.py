# strassen file - write as own function that takes in a matrix 
# take in n and crossover value, check if n is less than crossover value
# if n is less than crossover value, run matmul
import numpy as np

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
    if n > n0:
         #if n is even, we don't need to pad 
        if n%2 == 0: 
            A = M1[:n/2, :n/2]
            B = M1[:n/2, n/2:]
            C = M1[n/2:, :n/2]
            D = M1[n/2:, n/2:]
            E = M2[:n/2, :n/2]
            F = M2[:n/2, n/2:]
            G = M2[n/2:, :n/2]
            H = M2[n/2:, n/2:]

            P1 = strassen(A, F-H, n0) 
            P2 = strassen(A+B, H, n0)
            P3 = strassen(C+D, E, n0)
            P4 = strassen(D, G-E, n0)
            P5 = strassen(A+D, E+H, n0)
            P6 = strassen(B-D, G+H, n0)
            P7 = strassen(C-A, E+F, n0)

            ret = np.matrix(np.zeros((n, n)))
            ret[:n/2, :n/2] = P4 + P5 + P6 - P2
            ret[:n/2, n/2:] = P1 + P2
            ret[n/2:, :n/2] = P3 + P4
            ret[n/2:, n/2:] = P1 - P3 + P5 + P7

            return(ret)
        #if n is odd, we need to pad, and then recursively call again
        else:
            #inefficient padding
            padm1 = np.pad(M1, ((0, 1), (0,1)), mode = 'constant', constant_values = 0)
            padm2 = np.pad(M2, ((0, 1), (0,1)), mode = 'constant', constant_values = 0)
            return strassen(padm1, padm2, n0)[:n, :n]

    else: 
        return matmul(M1, M2)

test1 = np.matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
test2 = np.matrix([[1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0], [1, 0, 1, 0]])

print(strassen(test1, test2, 3))
print(test1[:3, :3])