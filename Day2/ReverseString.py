s = input("Enter String: ")

a = s.split()

for word in a:
    print(word[::-1], end=" ")