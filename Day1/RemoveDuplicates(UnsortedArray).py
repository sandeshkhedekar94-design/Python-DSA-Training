"""
Remove duplicates from unsorted array:

Question: Write a function to remove duplicates from an unsorted array.

Sample Input : [3, 2, 3, 1, 2, 4]
Expected output : [3, 2, 1, 4]
"""

arr = [3, 2, 3, 1, 2, 4]
ans = []
for x in arr:
    if x not in ans:
        ans.append(x)

print(ans)