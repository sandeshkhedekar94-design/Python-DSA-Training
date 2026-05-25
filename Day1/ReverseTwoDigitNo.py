num = int(input("Enter the 2- digit number: "))
reverse = (num % 10) * 10 + (num // 10)
print("Reversed Number =", reverse)