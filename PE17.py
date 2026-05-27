print("hello world")
sumtotal = 11

dic = {
    "1": 3,
    "2": 3,
    "3": 5,
    "4": 4,
    "5": 4,
    "6": 3,
    "7": 5,
    "8": 5,
    "9": 4,
    "0": 0
}
dicteen = {
    "10": 3,
    "11": 6,
    "12": 6, #twelve
    "13": 8, #THIRTEEN
    "14": 8,
    "15": 7,
    "16": 7,
    "17": 9,
    "18": 8,
    "19": 8 #NINETEEN
}
dictens = {
    "2": 6,
    "3": 6,
    "4": 5,
    "5": 5,
    "6": 5,
    "7": 7,
    "8": 6,
    "9": 6 #ninety
}


sumtohundred = 0

for n in range(1,100):
    nstr= str(n)
    while len(nstr) <3:
        nstr = "0"+nstr
    if nstr[1]=="0":
        sumtohundred += dic[nstr[2]]
        print(nstr, "sum now ", sumtohundred)
    elif nstr[1]=="1":
        sumtohundred += dicteen[nstr[1]+nstr[2]]
        print(nstr, "sum now ", sumtohundred)
    else:
        sumtohundred += dictens[nstr[1]]
        sumtohundred += dic[nstr[2]]
        print(nstr, "sum now ", sumtohundred)

sumofhundreds=0
for n in range(1,10):
    nstr=str(n)
    sumofhundreds += 7+dic[nstr]
    print(nstr, sumofhundreds)
print(sumofhundreds)

sumtotal += sumtohundred*10+ sumofhundreds*100+3*99*9
print(sumtotal)
