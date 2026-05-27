import numpy as np
with open('projecteuler67triangle.txt') as f:
    lines = f.readlines()
print(lines)

mate=[]
for line in lines:
    #row[0] = str(row[0])
    r = line
    emptylist=[]
    while r and r[:2]!="\n":
        emptylist.append(int(r[:2]))
        r=r[3:]
    mate.append(emptylist)
    print(emptylist)
    
for row in mate:
    print(row)

pathsum=mate

for rowindex in range(1,len(pathsum)):
    l = len(pathsum[rowindex])
    for index in range(l):
        print("bef:",l,index, pathsum[rowindex])
        if index==0:
            pathsum[rowindex][0]+=pathsum[rowindex-1][0]
        elif index==l-1:
            pathsum[rowindex][l-1]+=pathsum[rowindex-1][l-2]
        elif index<l-1: 
            pathsum[rowindex][index]+=max(pathsum[rowindex-1][index-1],pathsum[rowindex-1][index])
        print("aft:",l,index, pathsum[rowindex])
    #print(pathsum[rowindex])

for row in pathsum:
    print(row)
        
biggestnum=0
for num in pathsum[-1]:
    if num>biggestnum:
        biggestnum=num
print(biggestnum)

