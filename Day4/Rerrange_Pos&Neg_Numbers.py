arr = [-1,2,-3,4,5,-6]
pos = []
neg = []
ans1 = []
for i in range(len(arr)):
    if arr[i] >= 0:
        pos.append(arr[i])
    else:
        neg.append(arr[i])
for i in range(min(len(pos), len(neg))):
    ans1.append(neg[i])
    ans1.append(pos[i])
if len(pos) > len(neg):
    for i in range(len(neg), len(pos)):
        ans1.append(pos[i])
else:
    for i in range(len(pos), len(neg)):
        ans1.append(neg[i])
print(ans1)