import numpy as np

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

plist = primelist(100000)
blist = primelist(1000)

maxcount=0
for a in range(-999,1001,2):
    for b in blist:
        counter=0
        n=0
        while n**2+a*n+b in plist:
            counter+=1
            n+=1 
        if counter>30:
            print("a,b,counter= ", a,b,counter)
            if counter>maxcount:
                maxcount=counter
    #print(maxcount)
print(maxcount)

print("ferdig!")