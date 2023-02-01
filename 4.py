sum1=0
num1= int(input())
num=num1
while(num!=0):
    r=num%10
    sum1+=(r*r*r)
    num=num//10
if(sum1==num1):
    print("armstrong number")
else:
    print("not armstrong number")

'''#write a python program to make a list of cubes till the value n
cubes=[]
for i in range(11):
   cubes.append(i**3)
print(cubes)'''

'''#write a python program to find the absolute value for the difference in between even and odd digits of given numbers
num=[int(d) for d in str(input("enter number:"))]
even,odd=0,0
for i in range(0,len(num)):
    if i%2==0:
        even=even+num[i]
    else:
        odd=odd+num[i]
print(abs(odd-even))'''

'''cubes=[i**3 for i in range(11)]
print(cubes)'''
                         
'''print([i**3 for i in range(11)])'''

'''#company specific question
#geometric series 1,1,2,3,4,9,8,27,16,81...
term=int(input("enter the term"))
if term%2==0:
   term =term//2
   print(3**(term-1))
else:
    term= term//2+1
    print(2**(term-1))'''


