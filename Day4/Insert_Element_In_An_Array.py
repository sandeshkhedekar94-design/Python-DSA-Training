#Insertion of array.

arr = [1,2,3,4,5,6,7,8]
key = 22
loc = 3
n = int(input("Enter size: "))

for i in range(n):
    arr.append(int(input("Enter no: ")))

key = int(input("Enter element to insert: "))
loc = int(input("Enter location: ")) 

arr.insert(loc, key)
arr.append(0)

print("Updated array:", arr)