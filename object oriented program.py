#program to create and access an object
class abc:
    attribute1 =10
obj= abc()
print(obj.attribute1)

output:
    10

#program to create seif arg and access an obj
class xyz:
    var= 100
class abc:
    attribute1 =10
    def display(self):
        print("this is in class")
obj= abc()
print(obj.attribute1)
obj.display()

output:
    10
    this is in class

    
#program to check the usage of constructor
class abc:
    def __init__(self,value):
        print("this is in class")
        self.value= value
        print("the value is", value)
obj= abc(100)

output:
    this is in class
    the value is 100


#
class abc:
    class_var= 0
    def __init__(self,var):
        abc.class_var +=1
        self.var= var
        print(" obj value is ", var)
        print("class value is ", abc.class_var)
obj1= abc(100)
obj2= abc(101)
obj3= abc(102)

output:
class value is  1
 obj value is  101
class value is  2
 obj value is  102
class value is  3
