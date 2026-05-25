mob = input("Enter mobile number: ")

count = 0

for x in mob:
    if x >= '0' and x <= '9':
        count = count + 1

if count == 10 and (mob[0] == '6' or mob[0] == '7' or mob[0] == '8' or mob[0] == '9'):
    print("This Number is Valid")
else:
    print("This Number isn't Valid")
