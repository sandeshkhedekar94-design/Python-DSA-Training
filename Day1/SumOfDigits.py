no = int(input("Enter number: "))

sum = 0

while no > 0:
    rem = no % 10    #1234 % 10 = 4 ()
    sum = sum + rem
    no = no // 10

print("Sum of digits =", sum)