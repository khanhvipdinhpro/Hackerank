if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    dlist = list(arr)
    a = 0
    if n >= 2 and n <= 10 and n == len(dlist):
      for x in dlist:
       if x < -100 or x > 100:
        a = x
      if a < -100 or a > 100:
       pass
      else:
        maxx = max(dlist)
        newlist = [ z for z in dlist if z!= maxx ]
        maxxnew = max(newlist)
        print(maxxnew)