class MergeSort:
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        return self.merge(left, right)
    def merge(self, left, right):
        arr = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr.append(left[i])
                i += 1
            else:
                arr.append(right[j])
                j += 1
        while i < len(left):
            arr.append(left[i])
            i += 1
        while j < len(right):
            arr.append(right[j])
            j += 1
        return arr
    
if __name__ == '__main__':
    obj = MergeSort()
    arr = [9,12,123,45,35,13]
    print(obj.mergeSort(arr))