def hanoi(n, a, b ,c):
    if n>0:
        hanoi(n-1,a,c,b)
        if a:
            c.append(a.pop())
        hanoi(n-1,b,a,c)
a=[1,2,3,4]
b=[]
c=[]
print("before puzzle")
print(a,b,c)
hanoi(len(a),a,b,c)
print("after puzzle")
print(a,b,c)
