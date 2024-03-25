import numpy as np
import strassen

def make_graph(p):
    A = np.matrix(np.random.rand(1024, 1024))
    for i in range(1024):
        for j in range(1024):
            if A[i, j] < p:
                A[i, j] = 1
            else: 
                A[i, j] = 0
    return A

def count_triangles(A):
    A2 = strassen.strassen(A, A, 1024)
    A3 = strassen.strassen(A2, A, 1024)
    sum = 0
    for i in range(1024):
        sum = sum + A[i, i]
    return sum

def main():
    A = make_graph(0.01)
    count = count_triangles(A)
    print("p = 0.01: ", count)

    # for i in range(1024):
    #     for j in range(1024):
    #         print(A[i, j])

main()
