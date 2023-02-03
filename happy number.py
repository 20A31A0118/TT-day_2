def Happy_Number(n):
    if n == 1:
        return True
    sum,x=n,n
    while sum>9:
        sum =0
        while x>0:
            d = x%10
            sum += d*d
            x = int (x/10)
        if sum ==1:
            return True
        x = sum 
n=int(input("Enter a number:"))
if Happy_Number(n):
    print ("it is happy number:", n)
else:
    print("it is not a happy number:",n)
    
