import numpy as np
from itertools import permutations
listy=[0,1,2]
string= "absc"
lis123=[0,1,2,3,4,5,6,7,8,9]
#The lexicographic permutations of 0, 1 and 2 are:
#012   021   102   120   201   210
print(list(permutations(string)))
print(list(permutations(listy)))
a= list(permutations(lis123))
print(a[999999])