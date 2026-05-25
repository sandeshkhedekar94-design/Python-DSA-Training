no = int(input("Enter the Number: "))

temp = no
digits = 0

while temp > 0:
    digits = digits + 1
    temp = temp // 10

if digits % 2 == 0:

    half = digits // 2
    divisor = 1

    
    for i in range(half):
        divisor = divisor * 10

    first = no // divisor
    second = no % divisor

    sum = first + second

    if sum * sum == no:
        print("Tech Number")
    else:
        print("Not a Tech Number")

else:
    print("Not a Tech Number")