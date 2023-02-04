#write a program to check the given number is even or odd by using single stance class object with an attribute follwing a constructor
#test case:21
class number:
    even= 0
    def check(self,num):
        if num%2 == 0:
            self.even= 1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num, "is even")
        else:
            print(num, "is odd")
n= number()
n.even_odd(21)

output:
    21 is odd


class Number:
    even= []
    odd= []
    def __init__(self,num):
        self.num= num
        if num%2 ==0:
            Number.even.append(num)
        else:
            Number.odd.append(num)
n1= Number(11)
n2= Number(12)
n3= Number(13)
n4= Number(28)
n5= Number(7)
print("Even number list is:", Number.even)
print("Odd number list is:", Number.odd)

output:
    Even number list is: [12, 28]
    Odd number list is: [11, 13, 7]
    

