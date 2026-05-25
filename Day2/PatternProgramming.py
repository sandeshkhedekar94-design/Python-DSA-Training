'''

n = 65
for i in range(1,5):
    for j in range(1,5):
        print(chr(n),end="\t")
    n = n + 1
    print()

    '''

'''

for i in range(1,5):
    for j in range(1, i + 1):
        print(i,end="\t")
    print()

    '''
'''

for i in range(4,0,-1):
    for j in range(1, i + 1):
        print("*",end=" ")
    print()

'''

sp = 0
for i in range(4,0,-1):
    for x in range(sp):
        print(" ",end=" ")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
    sp = sp + 1 