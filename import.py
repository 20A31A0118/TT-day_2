#This the program to demonstrate match function using re-import
import re
str1 = "she sells sea shells at sea shore"
p1= "sells"
if re.search(p1,str1):
    print("match found")
else:
    print(p1, "not present in string")

import re
str1 = "she sells sea shells at sea shore"
p1= "sea"
rep = 'ocean'
ns=re.sub(p1,rep, str1, 1)
print(ns)

import re
p =r"[aeiou]"
if re.search(p,"clue"):
    print("matchy vowels")



