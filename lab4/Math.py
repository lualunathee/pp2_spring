#1 Write a Python program to convert degree to radian.
import math
a = int(input())
print((math.pi*a)/180)

#2 Write a Python program to calculate the area of a trapezoid.
a = int(input("Height: "))
b = int(input("Base, first value: "))
c = int(input("Base, second value: "))
print(((b+c)*a)/2)

#3 Write a Python program to calculate the area of regular polygon.
import math

def calc(n ,l):
    A = (n * (l**2))/(4 * math.tan(math.pi / n))
    return A
    
n = int(input())
l = int(input())
    
A = calc(n, l)
    
print(int(A))
#4 Write a Python program to calculate the area of a parallelogram.
a = int(input())
b = int(input())

Area = a * b

print(Area)