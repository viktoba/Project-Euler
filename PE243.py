import numpy as np

resilience_goal = 15499/94744

print(resilience_goal)

def compute_resilience_fraction(n):
    rescount =0
    for i in range(1,n):
        if i%2==0:
            continue
        elif i%3==0:
            continue
        elif i%5==0:
            continue
        elif i%7==0:
            continue
        elif i%11==0:
            continue
        elif i%13==0:
            continue
        elif i%17==0:
            continue
        elif i%19==0:
            continue
        elif i%23==0:
            continue
        #elif np.gcd(i,n) == 1:
            #print(i)
        rescount+=1
    frac = rescount/(n-1)
    #print(frac)
    return(frac)

primelist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]

for n in range(2, 5):
    resfrac = compute_resilience_fraction(n)
    if resfrac<0.5:
        print("Number: ", n, "Resfrac: ", resfrac)

numb=1
for k in range(len(primelist)):
    numb *= primelist[k]
    resfrac = compute_resilience_fraction(numb)
    if resfrac<0.4:
        print("Number: ", numb, "Resfrac: ", resfrac)

# numberlist = [2,3,6,12,30]
# for n in numberlist:
#     numb = n*2*3*5*7*11*13*17*19*23
#     resfrac = compute_resilience_fraction(numb)
#     if resfrac<0.4:
#         print("Number: ", numb, "Resfrac: ", resfrac)

print(resilience_goal)
print("done!")