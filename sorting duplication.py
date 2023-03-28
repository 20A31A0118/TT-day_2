list=[15,5,10,-5,25,-5,25,-5]
count={}
for i in list:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)       

list=[15,5,10,-5,25,-5,25,100,'d',97,'a']
count={}
for i in list:
    if str(i)==i:
        i=ord(i)
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
        
