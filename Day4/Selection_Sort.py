def selectionSort(arr):

    for i in range(len(arr)):
        min = i

        for j in range(i + 1, len(arr)):

            if arr[j] < arr[min]:
                min = j

        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp


if __name__ == '__main__':

    arr = [6,23,2,4,1,8,56,3]
    selectionSort(arr)
    print(*arr)
    print(arr)