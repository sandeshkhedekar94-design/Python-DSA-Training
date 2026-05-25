def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)

x = int(input("Enter base: "))
y = int(input("Enter power: "))

print("Answer:", power(x, y))