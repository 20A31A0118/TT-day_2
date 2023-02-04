#write a program that has class named use a class variable to define the values of constant phi. use this calss variable to calculate area and circumference of cirlce 
#with specified radius where radius is 7.5
class circle:
    pi = 3.14159
    def __init__(self,r):
        self.r=r
    def area(self):
        return circle.pi*self.r*self.r
    def circum(self):
        return 2*circle.pi*self.r
c= circle(7.5)
print("area=", c.area())
print("circumference=", c.circum())
    
output:
    area= 176.7144375
circumference= 47.12385
