import re
str=input("Enter any string: ")
m = re.match(str,"abc@xyz_pqr*")
if m!=None:
    print("Yes matching is available at beg")
    print('start index: ',m.star(),'. end index: ',m.end())