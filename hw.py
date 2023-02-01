'''n=int(input())
l=len(str(n))
s=0
for i in str(n):
    s+=int(i)**l
if s==n:
    print("armstrong number")
else:
    print("not armstrong number")'''
    
term=int(input("enter the term"))
if term%2==0:
    term=term//2
    print(7*(term))
else:
    term=term//2
    print(6*(term))
