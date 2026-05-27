import numpy as np
with open('projecteuler22names.txt') as f:
    lines = f.readlines()
print(lines[0])
list=[]
prev=-1
for char_index in range(len(lines[0])):
    if lines[0][char_index] == ",":
        list.append(lines[0][prev+2:char_index-1])
        prev=char_index
    elif char_index==len(lines[0])-1:
        print("Heyo!")
        print(lines[0][prev+2:char_index])
        list.append(lines[0][prev+2:char_index])

list.sort()
print(list[:150])
#print(list)
print(list[936:940])
print(list[:940])


alpha_dict = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
    'Z': 26
}

totalsum=0
for name_index in range(len(list)):
    namesum=0
    for letter in list[name_index]:
        namesum+= alpha_dict[letter]
        #print(letter,alpha_dict[letter],namesum)
    totalsum+=(name_index+1)*namesum
    print(list[name_index], namesum, name_index,(name_index)*namesum, totalsum)

print(totalsum)
print(list[-4:])


print("BRODERICK" in list)
print("ALONSO" in list)
print("MARY" in list)
print("PATRICIA" in list)
