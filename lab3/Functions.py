#Creating a function
#function is defined using the def keyword
#Example:
def my_function():
  print("Hello from a function")
  
#To call a function, use the function name followed by parenthesis:
#Example
def my_function():
  print("Hello from a function")

my_function()

#we can add as many arguments as you want, in this example we have only one argument
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Arbitrary functions
#If you do not know how many arguments that will be
#passed into your function, add a * before the parameter name
#Example
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
#Output:The youngest child is Linus

#You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#If the number of keyword arguments is unknown, add 
#a double ** before the parameter name:
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#if you send a List as an argument,
# it will still be a List when it reaches the function:
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
def myfunction():
  pass

#To specify that a function can have only positional arguments,
# add , / after the arguments:
def my_function(x, /):
  print(x)

my_function(3)

#To specify that a function can have only keyword arguments,
# add *, before the arguments:
def my_function(*, x):
  print(x)

my_function(x = 3)

#Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
#RECURSION
#Recursian Example:
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
#Output:
1
3
10
15
21

#EXERCIZE
#1 Create a function named my_function.
def my_function():
    print("Hello from a function")

#2 Execute a function named my_function.
def my_function():
  print("Hello from a function")
my_function()

#3 Inside a function with two parameters, print the first parameter.
def my_function(fname, lname):
    print(fname)
    
#4 Let the function return the x parameter + 5.
def my_function(x):
    return x + 5

#5 If you do not know the number of arguments that will be passed into your function,
#there is a prefix you can add in the function definition, which prefix?
def my_function(*kids):
    print("The youngest child is " + kids[2])
    
#6 If you do not know the number of keyword arguments that will be passed into your function,
# there is a prefix you can add in the function definition, which prefix?
def my_function(**kid):
    print("His last name is " + kid["lname"])