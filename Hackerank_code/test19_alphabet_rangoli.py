def print_rangoli(size):
    # your code goes here
    small_letter = list(map(chr,range(ord("a"),ord("z")+1)))
    a = 4*size-3
    b = " - ".join(small_letter).split()
    c = "".join(b)
    for i in range(1,size):
            top_matrix = b[b.index(small_letter[size - i]):(size*2-1)]
            top_matrix2 = list(top_matrix)
            top_matrix2.pop(0)
            top_matrix2.reverse()
            top_matrix3 = list(top_matrix2+top_matrix)
            d = "".join(top_matrix3)
            #print(small_letter[i].center(a," "))
            print(d.center(a,"-"))
    for i in range(size):
            top_matrix = b[b.index(small_letter[i]):(size*2-1)]
            top_matrix2 = list(top_matrix)
            top_matrix2.pop(0)
            top_matrix2.reverse()
            top_matrix3 = list(top_matrix2+top_matrix)
            d = "".join(top_matrix3)
            #print(small_letter[i].center(a," "))
            print(d.center(a,"-"))
"""def print_rangoli(size):
    # your code goes here
   letters = []
   for r in range(size*2-1):
    if r < size:
        letters.append(chr(96+size-r))
    else:
        letters.pop()
    print("-".join(letters+list(reversed(letters[:-1]))).center(4*size-3,"-"))"""

if __name__ == '__main__':
    n = int(5)
    print_rangoli(n)