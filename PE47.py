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

N=1000000
plist = primelist(N)

def distinct_prime_factors(n):
    factor_list=[]
    pindex=0
    while plist[pindex]<n+1:
        if n%plist[pindex]==0:
            factor_list.append(plist[pindex])
        pindex+=1
    return factor_list

d=0
length_list=[0]
for n in range(115000,N-10000):
    d = distinct_prime_factors(n)
    if len(d)==4:
        length_list.append(n)
        if length_list[-2]== n-1:
            if length_list[-3]== n-2:
                print(n, d, "  \tn-1: ", n-1, distinct_prime_factors(n-1), "\tn-2: ", n-2, distinct_prime_factors(n-2))
                if length_list[-4]== n-3:
                    print("HEYOYOHOHOYEOH\n\nSDFLKJ")
                    print(n, d, "  \tn-1: ", n-1, distinct_prime_factors(n-1), "\tn-2: ", n-2, distinct_prime_factors(n-2), "\tn-3: ", n-3, distinct_prime_factors(n-3))

         

for num in length_list:
    #print(num)
    if num+1 in length_list:
        #print(num, num+1)
        if num+2 in length_list:
            #print("WAHOO",num, num+1,num+2)
            if num+3 in length_list:
                print("WAHOO",num, num+1,num+2,num+3)

###answer: 134043
#   n:  134046 [2, 3, 11, 677]  
# n-1:  134045 [5, 17, 19, 83]    
# n-2:  134044 [2, 23, 31, 47]    
# n-3:  134043 [3, 7, 13, 491]

