"""#1 Create a generator that generates the squares of numbers up to some number N
 n = int(input())
 b = (i**2 for i in range(1, n))
 for value in b:
     print(value)


 #2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console.
 n = int(input())
 b = (i for i in range(1, n) if i)
 for value in b:
     if value%2==0:
         print(value, sep = ",")

 #3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
 n = int(input())
 b = (i for i in range(1, n) if i)
 for value in b:
     if value%3==0 and value%4==0:
         print(value, sep = ",")
        
#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.
b = int(input())
squares = (i**2 for i in range(a,b))
for i in squares:
    print(i)"""

#5 Implement a generator that returns all numbers from (n) down to 0
a = int(input())
squares = (i for i in range(0,a))
while a>0:
    a-=1
    print(a)
