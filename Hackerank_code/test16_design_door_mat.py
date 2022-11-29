if __name__ == '__main__':
    n,m = list(map(int,"8 24".split()))
    a = ".|."
    b = "-"
    # print upper
    for i in range(n//2):
        triangle_upper = (a*i).rjust(((m//2) -1),b) + a + (a*i).ljust(((m//2) -1),b)
        print (triangle_upper)
    # print middle
    print ("WELCOME".center(m,b))
    # print BOTTOM
    for i in range(n//2):
        triangle_upper = (a*((n//2-1)-i)).rjust(((m//2) -1),b) + a + (a*((n//2-1)-i)).ljust(((m//2) -1),b)
        print (triangle_upper)