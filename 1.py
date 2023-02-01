'''days=int(input())
if days<=84:
    calls=int(input())
    msgs=int(input())
    data=float(input())
    print("remaining days:",84-days)
    print("remaining calls:",3000-calls) if calls<=3000 else print("kindly top up")
    print("remaining msgs:",100-msgs) if msgs<=100 else print("msg failed")
    print("remaining data:",round((2-data),3)) if data<=2 else print("limit exceed")
else:
    print("your plan expired")'''

'''for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print("\n")'''

'''for i in range(65,91,2):
    for j in range(65,i+1,2):
        print(chr(i),end=" ")
    print("\n")'''

'''for i in range(1,11):
        print(i,"* 10=",i*10,end=" ")
        print("\n")'''

'''a=1
while(a<=10):
    print(a,"*5=",a*5)
    a=a+1'''

'''i=1
while(i<=10):
    j=1
    while(j<=i):
     print(j,end=" ")
     j=j+1
    print("\n")
    i=i+1'''

import math
a=5
b=3
c=4
print(math.sqrt(a*a+b*b+c*c))
