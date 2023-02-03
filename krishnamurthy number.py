import math
Number = int(input("Enter the number to check krishnamurthy number ="))
n = Number
sum = 0
while n>0:
    fact = 1
    rem = n%10
    fact = math.factorial(rem)
    sum = sum + fact
    n = n//10
if sum == Number:
    print(" it is krishnamurthy number:", Number)
else:
    print("it is not krishnamurthy number:", Number)
