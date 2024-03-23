import time

#
def experiments(A, B):
    crossover = [] #put crossover points here
    mult_time = [] #will hold times for each crossover point
    for i in range(0, len(crossover)):
        tic = time.perf_counter()
        strassen(A, B, crossover[i])
        toc = time.perf_counter()
        mult_time[i] = (toc - tic)

