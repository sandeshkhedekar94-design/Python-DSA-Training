"""

string1 = "hello"
string2 = ""

for i in range(len(string1)-1,-1,-1):
    string2 = string2 + string1[i]

print(string2)


"""

s= "ashish"

rev = ""
for x in s:
    rev = x + rev
print(rev)