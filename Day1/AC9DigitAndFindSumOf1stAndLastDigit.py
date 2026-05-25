no = int(input("Enter 9 digit no: "))

last = no % 10
first = no // 100000000

res = first + last

print("Sum =", res)