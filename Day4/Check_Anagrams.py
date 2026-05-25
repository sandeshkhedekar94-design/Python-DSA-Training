s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):
    print("Not Anagrams")

else:
    count1 = {}
    count2 = {}
    
    for ch in s1:
        if ch in count1:
            count1[ch] += 1
        else:
            count1[ch] = 1

    for ch in s2:
        if ch in count2:
            count2[ch] += 1
        else:
            count2[ch] = 1

    if count1 == count2:
        print("Anagrams")
    else:
        print("Not Anagrams")