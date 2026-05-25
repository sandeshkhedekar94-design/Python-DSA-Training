no = (int(input("Enter the Number: ")))
count = 0

while no > 0:
    no = no // 10
    count = count + 1
print(count)