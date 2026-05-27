import numpy as np
import itertools as iter

def sieve(N):
    boolist = [False,False]+[True]*(N-2)
    sqrt_N = int(np.ceil(np.sqrt(N))+1)
    for i in range(2,sqrt_N):
        if boolist[i]:
            for j in range(i**2,N,i):
                boolist[j]=False
    return boolist

def boolist_to_primelist(boolist):
    primelist=[]
    for i in range(len(boolist)):
        if boolist[i]:
            primelist.append(i)
    return(primelist)

def primelist(N):
    s = sieve(N)
    p = boolist_to_primelist(s)
    return(p)

plist = primelist(10000)
#print(plist)
oddlist=["1","3","5","7","9"]
evenlist=["2","4","6","8","0"]
list_of_permlists = []

for p in plist:
    if p<1000:
        continue
    pstr= str(p)
    pstrmod=list(pstr)
    l =list(iter.permutations(pstrmod, r=4))
    prime_perms=[]
    for permlist in l:
        permliststr=""
        for i in range(len(permlist)):
            permliststr+=permlist[i]
        permlistint = int(permliststr)
        if permlistint in plist:
            prime_perms.append(permlistint)
    if len(prime_perms)>2:
        print(p, len(prime_perms), "whole list:", prime_perms)
        list_of_permlists.append(prime_perms)

for prime_perm_list in list_of_permlists:
    list_of_diffs=[]
    lll= iter.permutations(prime_perm_list,r=3)
    for trip in lll:
        if trip[0]-trip[1]==trip[1]-trip[2] and trip[0]-trip[1] !=0:
            print("HEYO", trip, trip[0]-trip[1])
