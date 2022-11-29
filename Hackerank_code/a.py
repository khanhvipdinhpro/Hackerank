"""
b = "Hello, World!"

if b[2:len(b)] == b[2:]:
 b = 1
 print(b)
 
import random
print (random.randrange(100,10000))
"""
"""
txt = "We are the so-called \"Vikings\" fraom thae norath."
a = int((txt.find("a")))
c = 0
b = 0
while a != -1:
 txt=txt[a + 1:]
 c = b + a
 a = int((txt.find("a")))
 b = c + 1
 print(c)
"""
"""
# Python program to
# demonstrate return statement
 
def add(a, b):
 
    # returning sum of a and b
    return a + b
 
def is_true(a):
 
    # returning boolean of a
    return bool(a)
 
# calling function
res = add(2, 3)
print("Result of add function is {}".format(res))
 
res = is_true(2<5)
print("\nResult of is_true function is {}".format(res))
"""
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}