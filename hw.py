n=int(input())
l=len(str(n))
s=0
for i in str(n):
    s+=int(i)**l
if s==n:
    print("armstrong number")
else:
    print("not armstrong number")


#geometric series
#0,0,7,6,14,12,21,18,28,24,......
term=int(input("enter the term:"))
if term%2==0:
    term=term//2
    print(6*(term-1))
else:
    term=term//2+1
    print(7*(term-1))

#0,0,2,,1,4,2,6,3,8,4,10,5,12,6,14,7,16,8
term=int(input("enter the term:"))
if term%2==0:
    term=term//2
    print(1*(term-1))
else:
    term=term//2+1
    print(2*(term-1))
