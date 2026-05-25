a = "ABCDABBCDABBBCCCDDEEEF"

ans = ""

for x in a:
    if x not in ans:
        ans = ans + x
       
       
print(ans)