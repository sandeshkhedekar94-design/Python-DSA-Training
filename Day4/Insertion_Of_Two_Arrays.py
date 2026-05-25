arr1 = [1,2,3,4]
arr2 = [10,20]
arr3 = []
k = 2

print("Before Insertion:", arr1)

for i in range(len(arr2)):
    arr1.insert(k + i, arr2[i])

print("After Insertion:", arr1)