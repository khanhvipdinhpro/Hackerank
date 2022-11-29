import textwrap

def wrap(string, max_width):
    a = ""
    b = ""
    for i in range(len(string)):
        if (i + 1) % max_width == 0:
            b = a + string[i] + "\n"
            a = b
        else:
            b = a + string[i]
            a = b            
    return b

if __name__ == '__main__':
    string, max_width = "ABCDEFGHIJKLIMNOQRSTUVWXYZ", int(4)
    result = wrap(string, max_width)
    print(result)