import numpy as np
import strassen

v = 1024

def make_graph(p):
    A = np.matrix(np.random.rand(v, v))
    for i in range(v):
        for j in range(v):
            if A[i, j] < p:
                A[i, j] = 1
            else: 
                A[i, j] = 0
    return A

def count_triangles(A):
    A2 = strassen.strassen(A, A, v)
    A3 = strassen.strassen(A2, A, v)
    sum = 0
    for i in range(v):
        sum = sum + A3[i, i]
    return (sum / 6.0)

def main():
    for p in [0.01, 0.02, 0.03, 0.04, 0.05]:
        A = make_graph(p)
        count = count_triangles(A)
        print("p =", p, "-", count)

    # for i in range(1024):
    #     for j in range(1024):
    #         print(A[i, j])

main()
