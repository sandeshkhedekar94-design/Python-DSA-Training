no = int(input("Enter no: "))

save = no
sum = 0

while no > 0:
    rem = no % 10

    fact = 1
    i = 1

    while i <= rem:
        fact = fact * i
        i = i + 1

    sum = sum + fact
    no = no // 10

if save == sum:
    print("Peterson Number")
else:
    print("Not Peterson Number")