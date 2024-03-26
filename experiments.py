import time
import numpy as np
import strassen

#generate a list of random matrices
# each dimension generate 10 matrices -> 500, 1000, 1500 
matrixlist1 = [[0]*10]*3
matrixlist2 = [[0]*10]*3
i = 0 
for n in [250, 500, 750]:
    for j in range(10):
        matrixlist1[i][j] = np.matrix(np.zeros((n, n)))
        matrixlist2[i][j] = np.matrix(np.zeros((n, n)))
        for x in range(n):
            for y in range(n):
                matrixlist1[i][j][x,y] =  np.random.choice([0,1])
                matrixlist2[i][j][x,y] =  np.random.choice([0,1])
    i += 1

#experiments
def experiments():
    crosspoints = list(range(200, 500)) #put crossover points here
    mult_time = [[0]*len(crosspoints)]*3 #3 sublists, each with the crosspoint times 
    #these are all the crossover points
    for i in range(3):
        for cross in crosspoints:
            sum = 0
            for j in range(10):
                tic = time.time()
                strassen.strassen(matrixlist1[i][j], matrixlist2[i][j], cross)
                toc = time.time()
                sum += toc - tic
            mult_time[i][cross] = sum/10
    return(mult_time)
    
    
    # for matrix in matrixlist:
    #     for cross in range(1, crosspoints):
    #         tic = time.perf_counter()
    #         strassen.strassen(A, B, cross)
    #         toc = time.perf_counter()
    #         mult_time[cross] = (toc - tic)

    
print(experiments())