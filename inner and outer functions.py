def outf():
    var = 10
    def innf():
        var = 20
        print("inner var",var)
    innf()
    print("outer var",var)
outf()


#write a program with a user defined function which returns an integer value to the caller
def cube(x):
    return(x*x*x)
num= 10
result = cube(num)
print("output of the evaluation is", result)


#write a program to act 6 user defined values and return the values to the main function
# 8 6 4 2 10 0
def sum(a,b,c,d,e,f):
    return(a+b+c+d+e+f)
a=8
b=6
c=4
d=2
e=10
f=0
result = sum(a,b,c,d,e,f)
print("output of the evaluation is", result)



def display(name, age):
    print("name",name)
    print("age",age)
n= "vj"
y= 77
display(name=n, age=y)
