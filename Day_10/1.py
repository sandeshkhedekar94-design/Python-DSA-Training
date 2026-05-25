import re
x = "[abc]"
x = "[^abc]"
x = "[a-z]"
x = "[0-9]"
x = "[a-zA-Z0-9]"
x = "[^a-zA-Z0-9]"
matcher=re.finditer(x, "a75t@$t6784265^")
for match in matcher:
    print(match.start(),'...',match.group())