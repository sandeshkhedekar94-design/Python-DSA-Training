no = int(input("Enter 3 digit no: "))

n1 = no % 10
no = no // 10

n2 = no % 10
no = no // 10

n3 = no % 10

reverse = (n1 * 100) + (n2 * 10) + n3

print("Reverse =", reverse)