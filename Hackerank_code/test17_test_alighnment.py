if __name__ == '__main__':
    #Enter your code here. Read input from STDIN. Print output to STDOUT

    thickness = int(input()) #This must be an odd number
    a = 'H'

    #Top Cone
    for i in range(thickness):
        print((a + a*i*2).center(thickness*2-1, " "))

    #Top Pillars
    for i in range(thickness + 1):
        print((a*thickness).center(thickness*2-1," ")+ 2*(thickness)*" "+ " " + (a*thickness).center(thickness*2-1," "))

    #Middle Belt
    for i in range((thickness + 1) //2):
        print((a*(thickness + int((thickness - 1)/2))).rjust(thickness*2-1," ")+ 2*(thickness)*a+ a  + (a*(thickness + int(thickness/2))).ljust(thickness*2-1," "))     

    #Bottom Pillars
    for i in range(thickness + 1):
        print((a*thickness).center(thickness*2-1," ")+ 2*(thickness)*" "+ " "  + (a*thickness).center(thickness*2-1," "))     

    #Bottom Cone
    for i in range(thickness):
        print((2*thickness+ 2*thickness - 1)*" "+ " "  + (a + a*(thickness - i - 1)*2).center(thickness*2-1, " "))