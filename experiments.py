import time
import numpy as np
import strassen
import matmul


naivelist = []
strassenlist = []
for n in range(10, 20):
    #generate a matrix of size n:
    matrix1 = np.matrix(np.zeros((n,n)))
    matrix2 = np.matrix(np.zeros((n,n)))
    for x in range(n):
        for y in range(n):
            matrix1[x,y] =  np.random.choice([0,1])
            matrix2[x,y] =  np.random.choice([0,1])
    if n%2 == 0: #if n is even
        ticstras = time.time()
        strassen.strassen(matrix1, matrix2, n/2)
        tocstras = time.time()
        #strassenlist.append(tocstras - ticstras)
        print(n, "strassen:", tocstras - ticstras)
    else: 
        ticstras = time.time()
        strassen.strassen(matrix1, matrix2, n-1)
        tocstras = time.time()
        #strassenlist.append(tocstras - ticstras)
        print(n, "strassen:", tocstras - ticstras)

    
    ticnaive = time.time()
    matmul.matmul(matrix1, matrix2)
    tocnaive = time.time()
    #naivelist.append(tocnaive - ticnaive)
    print(n, "naive:", tocnaive - ticnaive)

# print(naivelist)
# print(strassenlist)

#graph stuff now! 



# #generate a list of random matrices
# # each dimension generate 10 matrices -> 500, 1000, 1500 
# matrixlist1 = [[0]*10]*3
# matrixlist2 = [[0]*10]*3
# i = 0 
# for n in [250, 500, 750]:
#     for j in range(5):
#         matrixlist1[i][j] = np.matrix(np.zeros((n, n)))
#         matrixlist2[i][j] = np.matrix(np.zeros((n, n)))
#         for x in range(n):
#             for y in range(n):
#                 matrixlist1[i][j][x,y] =  np.random.choice([0,1])
#                 matrixlist2[i][j][x,y] =  np.random.choice([0,1])
#     i += 1

# #experiments
# def experiments():
#     crosspoints = list(range(256, 512, 50)) #put crossover points here
#     mult_time = [[0]*len(crosspoints)]*3 #3 sublists, each with the crosspoint times 
#     #these are all the crossover points
#     for i in range(3):
#         for cross in crosspoints:
#             sum = 0
#             for j in range(5):
#                 tic = time.time()
#                 strassen.strassen(matrixlist1[i][j], matrixlist2[i][j], cross)
#                 toc = time.time()
#                 sum += toc - tic
#             print(sum/5)
#             #mult_time[i][cross] = sum/10
#     return(mult_time)
    
    
#     # for matrix in matrixlist:
#     #     for cross in range(1, crosspoints):
#     #         tic = time.perf_counter()
#     #         strassen.strassen(A, B, cross)
#     #         toc = time.perf_counter()
#     #         mult_time[cross] = (toc - tic)

    
# print(experiments())