"""
d = {}
d[100] = "Ashish"
d[200] = "Prashant"
d[300] = "Sandip"
print(d)
print([d])

"""

rec = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    per = float(input("Enter percentage: "))

    rec[name] = per

print("\nStudent Record:")
print(rec)

print("\nName\tPercentage")

for x in rec:
    print(x, "\t", rec[x])