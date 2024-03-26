import time
import numpy as np
import strassen
import matmul
import matplotlib.pyplot as plt


naivelist = []
strassenlist = []
nvals = list(range(3, 60))
for n in nvals:
    #generate a matrix of size n:
    matrix1 = np.matrix(np.zeros((n,n)))
    matrix2 = np.matrix(np.zeros((n,n)))
    sums = 0
    sumn = 0
    for i in range(3): #taking averages
        for x in range(n):
            for y in range(n):
                matrix1[x,y] =  np.random.choice([0,1])
                matrix2[x,y] =  np.random.choice([0,1])
        ticstras = time.time()
        strassen.strassen(matrix1, matrix2, n-1)
        tocstras = time.time()
        #strassenlist.append(tocstras - ticstras)
        sums += tocstras - ticstras
    avgs = sums/3
    print(n, "strassen:", avgs)
    strassenlist.append(avgs)

    for i in range(3):
        ticnaive = time.time()
        matmul.matmul(matrix1, matrix2)
        tocnaive = time.time()
        sumn += tocnaive - ticnaive
    #naivelist.append(tocnaive - ticnaive)
    avgn = sumn/3
    print(n, "naive:", avgn)
    naivelist.append(avgn)

# print(naivelist)
# print(strassenlist)

#graph stuff now! 

plt.plot(nvals, strassenlist, label = "strassen")
plt.plot(nvals, naivelist, label = "naive")

#label it 
plt.xlabel('n')
plt.ylabel('runtime')
plt.title('naive vs. strassen')
plt.legend()  # Adding legend


plt.show()

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