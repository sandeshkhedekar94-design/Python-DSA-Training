no = int(input("Enter 6 digit number: "))

save = no
count = 0

while no > 0:
    no = no // 10
    count = count + 1

no = save

if count == 6:


    n1 = no // 1000
    n2 = no % 1000

    sum = n1 + n2

    sq = sum * sum

    if sq == no:
        print("Tech Number")
    else:
        print("Not Tech Number")

else:
    print("Enter only 6 digit number")