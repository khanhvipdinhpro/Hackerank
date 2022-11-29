def print_formatted(number):
    # your code goes here
    for i in range(1,number+1):
        print(("{:d}".format(i)).rjust(len("{:b}".format(number)), " ")+ ("{:o}".format(i)).rjust(len("{:b}".format(number)) + 1, " ") + ("{:X}".format(i)).rjust(len("{:b}".format(number)) + 1, " ") + ("{:b}".format(i)).rjust(len("{:b}".format(number))+1, " "))
if __name__ == '__main__':
    n = int(5)
    print_formatted(n)
    print("{:.5f}".format(2.3333333).rjust(10, "-"))
    print("{:*^11.2f}".format(12.2).center(20,"o"))
    print(r"\110\145\154\154\157")