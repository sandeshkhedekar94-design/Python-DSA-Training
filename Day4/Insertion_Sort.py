def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = j + 1
arr = [5,2,17,2,4,9,15,1]


for i in range(1,len(arr)):
    current=arr[i]
    pos=i
    while current<arr[pos-1] and pos>0:
        arr[pos]=arr[pos-1]
        pos=pos-1
    arr[pos]=current
print(arr)