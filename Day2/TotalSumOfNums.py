# accept values from user & find sum of list

n = int(input("Enter size: "))

arr = []

print("Enter list elements: ")

for i in range(n):
    ele = int(input("Enter element: "))
    arr.append(ele)

sum = 0

for i in range(len(arr)):
    sum = sum + arr[i]

print("Sum =", sum)