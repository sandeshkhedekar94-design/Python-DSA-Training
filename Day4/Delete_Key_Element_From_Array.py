#Deletion of Array

arr = [1,2,3,4,5,6,7,8]

loc = 4

print("Before Delete:", arr)

for i in range(loc + 1, len(arr)):
    arr[i - 1] = arr[i]

arr.pop()

print("After Delete:", arr)