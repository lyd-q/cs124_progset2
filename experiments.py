import time
import numpy as np
import strassen
import matmul
import matplotlib.pyplot as plt


naivelist = []
strassenlist = []
nvals = list(range(4, 15))
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
