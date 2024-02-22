"""#1
def ountogram(a):
  print(28.3495231 * a)
  
a = int(input())
ountogram(a)


#2
def FtoC(b):
  print((5*(b-32))/9)
  
b = int(input())
FtoC(b)

#3
def solve(numheads, numlegs):
  b = int((numlegs - 2*numheads)/2)
  a = int(numheads-b)
  print(a,b)
  
a = (int(input()))
b = (int(input()))
print(solve(a,b))

#4
def filter_prime(n):
  if n<=1:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n%i==0:
      return False
  return True

list1 = [3, 4 , 6, 7, 13, 20, 12, 15, 17]
for i in list1:
  if filter_prime(i):
    print(i)
    
#5
import itertools
def stringP(str):
  str1 = itertools.permutations(str)  #creates an iterator str1
  str1 = [''.join(permutation) for permutation in str1] #iterates over each permutation in str1
  print(str1)

str2 = input()
stringP(str2)

#6
def rev(sentence):
  words = sentence.split()
  rev_words = words[::-1]
  rev_sent = ' '.join(rev_words)
  return rev_sent

str3 = input()
print(rev(str3))

#7
def has_33(nums):
  for i in range(len(nums)-1):
    if nums[i] == 3 and nums[i+1]==3:
      return True
  return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3])) 

#8
def spy_game(nums):
  h0 = False
  h00 = False
  h007 = False
  for i in nums:
    if i == 0 and not h0:
      h0 = True
    elif i == 0 and h0 and not h00:
      h00 = True
    elif i == 7 and h0 and h00:
      h007 = True
  return h007    

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]) )
print(spy_game([1,7,2,0,4,5,0]))
      
#9
def volume(r):
    V = (4/3)*3.14*(r**3)
    return V
    
r = float(input())
print(volume(r))

#10
def unique(list):
    numbers = []
    for i in list:
        if i not in numbers:
            numbers.append(i)
    return numbers
        
spy_game = ([1,8,2,4,0,0,7,8,5])
print(unique(spy_game)) """

#11
def palin(n):
  rev = n[::-1]
  if n == rev:
    return True
  return False

str4 = input()
print(palin(str4))

#12
def histogram(n):
  for i in range(len(n)):
    print('*'*n[i])
  
histog = ([4, 9, 7])
print(histogram(histog))

#13
import random #to generate a random number
def guess():
  numgues = 0
  num = random.randint(1, 20)
  a = input("Hello! What is your name?")
  b = input("Well, {a}, I am thinking of a number between 1 and 20.")
  while True:
    c = int(input("Take a guess. "))
    numgues += 1
    if c < num:
      print("Your guess is too low.")
    elif c > num:
      print("Your guess is too high.")
    else:
      print("Good job, KBTU! You guessed my number in {numgues} guesses!")
      break

guess()

