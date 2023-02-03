def vj(money):
    print("give vijay the sum of",money)
vj(50)


def vj(money):
    print("give vijay the sum of",money)
vj(5*10)


def vj(money):
    print("give vijay the sum of",money)
money=50    
vj(money)


#global variable and local variable
var = 'vijay'
def show():
    global var1
    var1 = 'tall'
    print("in fuction var is", var)
show()
print("outside function", var1)
print("var is", var)
