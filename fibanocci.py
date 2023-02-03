#write a program to print the fibanocci series using recursion function
def fib(n):
    if n<2:
        return 1
    return (fib(n-1)+fib(n-2))
n= int(input())
for i in range (n):
    print("fibonacci (",i,")",fib(i))
