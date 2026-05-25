# sum of even and odd numbers

n = int(input("Enter size: "))

arr = []
even = 0
odd = 0


for i in range(n):
    ele = int(input("Enter number: "))
    arr.append(ele)

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even = even + arr[i]
    else:
        odd = odd + arr[i]

print("Sum of even numbers =", even)
print("Sum of odd numbers =", odd)