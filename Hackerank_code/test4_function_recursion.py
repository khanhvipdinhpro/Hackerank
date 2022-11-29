"""
#cach 1
if __name__ == '__main__':
    n = int(input())
    a = ""
    b = ""
    i = 1
    if n >= 1 and n <= 150:
     while i <= n:
        a = b
        b = a + str(i)
        i += 1
     print(b)
"""

# cach 2
if __name__ == '__main__':
   n = int(input())
   def tri_recursion(n):
     if n == 1:
      return 1
     elif n > 1 and n <= 150:
      result = str(n) + str(tri_recursion(n - 1))
      return(result)
   a = tri_recursion(n)
   i = "1"
   while i in a:
      i = str(int(i) + 1)
      b = str(int(i) - 1)
      print(b, end = "")

"""
if __name__ == '__main__':
   n = int(input())
   def tri_recursion(n):
     if n == 1:
      return 1
     elif n > 1 and n <= 150:
      result = str(n) + str(tri_recursion(n - 1))
      return result
   print (tri_recursion(n))
   """