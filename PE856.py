import numpy as np
from itertools import permutations
import random
import timeit

deck = []
for i in range(52):
    deck.append(i%13)
print(deck)


N=100000

start = timeit.default_timer()
print("The start time is :", start)

def draw_cards(deck):
    pair_index_list=[]
    a= random.sample(deck,52)
    for index in range(52):
        if (a[(index-1)%52]==a[index%52]):
            pair_index_list.append(index)
    if pair_index_list ==[]:
        print(pair_index_list, "sum = ", 52*52)
        return 52*52
    elif len(pair_index_list)==1:
        print(pair_index_list, "sum = ", 1429)
        return 1429
    pair_index_list+=[pair_index_list[0]+52]
    #print(pair_index_list)
    sum=0
    for pair_index_index in range(1,len(pair_index_list)):
        diff= pair_index_list[pair_index_index]-pair_index_list[pair_index_index-1]
        #print("diff, sum",diff, diff*(diff+3)//2)
        sum+=diff*(diff+3)//2
    print(pair_index_list, "sum = ", sum)
    return sum




tot=0
for n in range(N):
    tot+= draw_cards(deck)

print("tot = ", tot, "52*N=", 52*N)
avg = tot/(52*N)
print("avg = ", avg)
print("The difference of time is :",
              timeit.default_timer() - start)



start2 = timeit.default_timer()
print("The start time is :", start2)

def draw_num():
    no_pair=True
    a= [0]+random.sample(range(1,52), 51)
    index=1
    while no_pair and index<52:
        if (a[index-1]-a[index])%13==0:
            #print(index, a[index-1]%13,a[index]%13)
            return index
        index+=1
    return 52

tot=0
for n in range(N):
    tot+= draw_num()

print("tot = ", tot, "N=", N)
avg = tot/N
print("avg = ", avg)

print("The difference of time is :",
              timeit.default_timer() - start2)

start2 = timeit.default_timer()
print("The start time is :", start2)

# def draw_num2():
#     no_pair=True
#     a= [0]+random.sample(range(1,52), 51)
#     index=1
#     partialsum=0
#     for num in a:
#         temp=partialsum
#         partialsum+=(-1)**index *num
#         if temp
#         index+=1
        
#     while no_pair and index<52:
#         if (a[index-1]-a[index])%13==0:
#             #print(index, a[index-1]%13,a[index]%13)
#             return index
#         index+=1
#     return 52

# tot=0
# for n in range(N):
#     tot+= draw_num2()

# print("tot = ", tot, "N=", N)
# avg = tot/N
# print("avg = ", avg)

# print("The difference of time is :",
#               timeit.default_timer() - start2)
