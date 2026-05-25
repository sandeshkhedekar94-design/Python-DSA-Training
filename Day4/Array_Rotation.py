arr = [5,1,2,3,4]

print("Before Rotation:", arr)

temp = arr[len(arr)-1]

for i in range(len(arr)-1, 0, -1):
    arr[i] = arr[i-1]

arr[0] = temp

print("After Rotation:", arr) 