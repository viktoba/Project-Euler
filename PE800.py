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

plist = primelist(31000000) #add 0
pshortlist = primelist(950000)
#print(plist)
c = 800800*np.log2(800800)
smallc = 800*np.log2(800)
print(len(plist))
#c=smallc
ploglist= []
for p in plist:
    ploglist.append(np.log2(p))
#print(ploglist)
plistminus1 = plist[1:]
counter=0
maxp=0
for p in plist:
    pindex = plist.index(p)
    while p*np.log2(p) + p*np.log2(p)<c:
        counter+=pindex
        print(p, counter)
        maxp=p
        break
    qindex=0
    while 2*p*np.log2(p)>c and plist[qindex]<p and p*np.log2(plist[qindex]) + plist[qindex]*np.log2(p)<c:
        counter+=1
        qindex+=1
    if p<10000:
        print(p,counter,plist[qindex])

print(counter)


# prev_breaking_qindex=10
# counter=0
# qqqindex=-1
# for p in pshortlist:
#     #logp = np.log2(p)
#     pindex = plist.index(p)
#     logp = ploglist[pindex]
#     c_over_logp= c/logp
#     pindex = plist.index(p)
#     # if prev_breaking_qindex-pindex==0:
#     #     break
#     # elif pindex>4:
#     #     quickstart = int(np.ceil((prev_breaking_qindex-pindex)*(np.log2(plist[pindex]))))
#     # else:
#     #     
#     ##quickstart=1
#     qindex = qqqindex
#     if qqqindex <= pindex:
#         qindex= pindex+1
#     tempcounter=0
#     tempcounter+=qindex-pindex-1
#     while qindex>pindex and qindex<len(plist) and plist[qindex]*logp + p*ploglist[qindex]<c:
#         #counter+=1
#         tempcounter+=1
#         qindex+=1
#     if tempcounter>0:
#         counter+=tempcounter
#     prev_breaking_qindex = qindex-1
#     quickstart = (prev_breaking_qindex-pindex)//2
#     # while qindex>pindex and qindex<len(plist) and plist[qindex]<c_over_logp:
#     #     if plist[qindex]<c_over_logp/2:
#     #         counter+=1
#     #         qindex+=1
#     #     elif plist[qindex]*logp + p*np.log2(plist[qindex])<c:
#     #         counter+=1
#     #         qindex+=1
#     # for q in plist:
#     #     if q>p:
#     #         n = q*logp + p*np.log2(q)
#     #         if n<c:
#     #             counter+=1
#         #print(p,counter, tempcounter, np.log2(plist[pindex])-np.log2(plist[pindex-1]))
#         #print(p,counter, tempcounter, np.log2(tempcounter), (c/(2*p*ploglist[pindex])), (c/(2*ploglist[pindex])))
#     qqqindex = pindex
#     while plist[qqqindex]<(c/(2*ploglist[pindex])) and plist[qqqindex]<len(plist):
#         qqqindex+=1
#     qqqindex-=1
#     if p<1000:
#         print(p,counter, tempcounter, np.log2(tempcounter), (c/(2*p*ploglist[pindex])), (c/(2*ploglist[pindex])), qqqindex-pindex, plist[qqqindex])
#     #print(p,counter, tempcounter, np.log2(tempcounter), qqqindex-pindex, plist[qqqindex])
#     #print(p,counter)

# print(counter)

