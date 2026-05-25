import re

number = input("Enter mobile number: ")

match = re.fullmatch("[6-9][0-9]{9}", number)

if match:
    print(number, "is valid mobile number")
else:
    print(number, "is invalid mobile number")