import numpy as np
input = np.loadtxt("projecteuler81matrix.txt", dtype='i', delimiter=',')
print(input)
summatrix= input
print(summatrix)
for i in range(1,80):
    summatrix[0][i]= input[0][i]+summatrix[0][i-1]

for j in range(1,80):
    summatrix[j][0]= input[j][0]+summatrix[j-1][0]

for i in range(1,80):
    for j in range(1,80):
        summatrix[j][i] = input[j][i]+min(summatrix[j-1][i],summatrix[j][i-1])
        print("j,i= ", j, i, "summatrix[j][i] = ", summatrix[j][i])

print(summatrix)
#PE answer is
print(summatrix[79][79])