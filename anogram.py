'''n=int(input())
sn=input()
m=0
c=0
for i in range(n):
    if(sn[i]=="1"):
        c+=1
    else:
        m=max(c,m)
        c=0
print(m)'''


size =int(input("enter the size of binary"))
max=count=flag= 0
x=input()
arr=list(x)
for i in range(0, size):
    if arr[i]== '1':
       count=count+ 1;
       flag= 1;
    elif(arr[i]=='0' and flag ==1):
        count=0
        flag=0
    if count >max:
        max=count
print(max)
        
