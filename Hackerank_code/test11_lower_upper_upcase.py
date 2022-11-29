#Swap Case
def swap_case(s):
  a = ""
  b = ""
  if len(s) > 0 and len(s) <= 1000:
    for i in s:
        if i == i.lower():
            i = i.upper()
        elif i == i.upper():
            i = i.lower()
        elif i == " ":
            i == " "
        a = b + i
        b = a
    return b
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)