def is_leap(year):
    leap = False
    if year <= 2000:
      n = (2000 - year) % 4
      if year % 100 == 0 and year % 400 == 0:
            leap = True
      elif year % 100 == 0 and year % 400 != 0:
            leap = False
      elif n == 0:
            leap = True
      else:
            leap = False
    elif ( year > 2000) and ( year < pow(10,5)):
      n = (year - 2000) % 4
      if year % 100 == 0 and year % 400 == 0:
            leap = True
      elif year % 100 == 0 and year % 400 != 0:
            leap = False
      elif n == 0:
            leap = True
      else:
            leap = False
    # Write your logic here
    
    return leap

year = int(input())
print(is_leap(year))