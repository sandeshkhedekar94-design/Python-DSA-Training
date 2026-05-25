no = int(input("Enter no: "))

temp = no
sum = 0
count = len(str(no))

while no > 0:
    rem = no % 10
    sum = sum + (rem ** count)
    no = no // 10

if temp == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")