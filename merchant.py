def findTotalCurtains(n,numbers):
    total = 0
    for i in numbers:
        total += i//2
    return total
n = int(input())
numbers = list(map(int, input().split()))
print(findTotalCurtains(n,numbers))
