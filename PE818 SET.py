from itertools import permutations

list_of_cards=[]
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                list_of_cards.append([i,j,k,l])
print(list_of_cards)
print("num of cards:",len(list_of_cards))
#print(list(permutations(list_of_cards,3)))
print("num of 3-card collections:",len(list(permutations(list_of_cards,3))))
list_of_sets=[]
for card1 in list_of_cards:
    for card2 in list_of_cards:
        if card2 > card1:
            card3=[]
            card3.append((-card1[0]-card2[0])%3)
            card3.append((-card1[1]-card2[1])%3)
            card3.append((-card1[2]-card2[2])%3)
            card3.append((-card1[3]-card2[3])%3)
            #print(card1,card2,card3)
            if card3>card2:
                list_of_sets.append([card1,card2,card3])

def count_sets(cards):
    count=0
    for card1 in cards:
        for card2 in cards:
            if card2 > card1:
                for card3 in cards:
                    if card3>card2:
                        if (card1[0]+card2[0]+card3[0])%3==0 and (card1[1]+card2[1]+card3[1])%3==0 and (card1[2]+card2[2]+card3[2])%3==0 and (card1[3]+card2[3]+card3[3])%3==0:
                            count+=1
                # card3=[]
                # card3.append((-card1[0]-card2[0])%3)
                # card3.append((-card1[1]-card2[1])%3)
                # card3.append((-card1[2]-card2[2])%3)
                # card3.append((-card1[3]-card2[3])%3)
                # if card3 in cards and card3>card2:
                #     #print("SET!")
                #     count+=1
    return count


print("num of sets:",len(list_of_sets))
#num of sets is 81C2 / 3C2
#wlog point 0 and point 1 are always [0,0,0,0], [0,0,0,1].
# a = list(permutations(list_of_cards[3:],3))
# b = []
# for cards in a:
#     bcards = [[0,0,0,0],[0,0,0,1],[0,0,0,2]]+list(cards)
#     b.append(bcards)
# print(b[:5])
# print(len(b))


# sum=0
# for cards in b:
#     c= count_sets(cards)
#     sum+=c
# print("sum=", sum)
# print("sum * 81*80/3!=", sum*81*80//(3*2*3))


# a = list(permutations([list_of_cards[2]]+list_of_cards[4:],3))
# b = []
# for cards in a:
#     bcards = [[0,0,0,0],[0,0,0,1],[0,0,1,0]]+list(cards)
#     b.append(bcards)
# print(b[:5])
# print(len(b))

# sum=0
# for cards in b:
#     c= count_sets(cards)
#     sum+=c
# print("sum=", sum)
# print("sum * 81*80/3!=", sum*81*80//(3*2*3))

a = list(permutations(list_of_cards[4:],2))
b = []
for cards in a:
    bcards = [[0,0,0,0],[0,0,0,1],[0,0,0,2],[0,0,1,0]]+list(cards)
    b.append(bcards)
print(b[:5])
print(len(b))

sum=0
for cards in b:
    c= count_sets(cards)
    sum+=c
print("sum=", sum)
print("sum * 1080*78*15/4=", sum* 1080*78//4)