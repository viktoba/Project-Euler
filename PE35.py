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

plist = primelist(1000000)
#print(plist)
oddlist=["1","3","5","7","9"]
evenlist=["2","4","6","8","0"]
cyclist=[]

for p in plist: 
    pstr= str(p)
    cyclic=True
    for pstrdigit in pstr:
        if pstrdigit in evenlist: #removes 2, so need to add 1 at the end
            cyclic=False
            break
    pstrmod=list(pstr)
    for n in range(len(pstr)):
        pstrmod.append(pstrmod.pop(0))
        pstrmodstr=""
        for i in range(len(pstrmod)):
            pstrmodstr+=pstrmod[i]
        pstrmodint = int(pstrmodstr)
        if pstrmodint not in plist:
            cyclic=False
            break
    if cyclic:
        cyclist.append(pstr)
        print(pstr)

cyclist.append("2")
print(cyclist)
print(len(cyclist))


    


