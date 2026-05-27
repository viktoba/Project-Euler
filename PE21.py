import numpy as np
import itertools

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

N=100000
plist=primelist(N)

def distinct_prime_factors(n):
    factor_list=[]
    pindex=0
    while plist[pindex]<n+1:
        if n%plist[pindex]==0:
            factor_list.append(plist[pindex])
        pindex+=1
    return factor_list

def find_multiplicity(n):
    distinct = distinct_prime_factors(n)
    dist_multiplicity=[]
    for d in distinct:
        d_pow=d
        mult=1
        while n%d_pow ==0:
            d_pow*=d
            mult+=1
        mult-=1
        dist_multiplicity.append(mult)
    return dist_multiplicity

def find_divisors(n):
    dist= distinct_prime_factors(n)
    #print("dist",dist)
    list_of_divs= []
    mult_list= find_multiplicity(n)
    #print("mult_list",mult_list)
    list_leq_mult_list=[]
    for mult in mult_list:
        temp_list=[]
        for i in range(mult+1):
            temp_list.append(i)
        list_leq_mult_list.append(temp_list)
    #print("list_leq_mult_list", list_leq_mult_list)
    for element in itertools.product(*list_leq_mult_list):
        k=1
        for pindex in range(len(dist)):
            k*=dist[pindex]**element[pindex]
            #print(k)            
        #print(k, element)
        list_of_divs.append(k)
    return list_of_divs

def add_divs(n):
    div_list=find_divisors(n)[:-1]
    sum=0
    for num in div_list:
        sum+=num
    return sum

amicable_list=[]
for n in range(10000):
    s = add_divs(n)
    if s!=n and add_divs(s)==n:
        amicable_list.append(n)
        print(n,s)

print(amicable_list)
sum=0
for num in amicable_list:
    sum+=num
print(sum)
    

    


