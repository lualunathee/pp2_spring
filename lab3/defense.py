def getmax(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

a=int(input())
b=int(input())
c=int(input())
maxvalue = getmax(a,b,c)
print(maxvalue)


def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

a = int(input())
value = fibonacci(a)
print(value)