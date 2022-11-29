#List basic
if __name__ == '__main__':
    newlist = []
    N = int(input())
    for i in range(N):
        name, *line = input().split()
        value = list(map(int,line))
        if name == "insert":
            newlist.insert(value[0], value[1])
        elif name == "print":
            print (newlist)
        elif name == "remove":
            newlist.remove(value[0])
        elif name == "append":
            newlist.append(value[0])
        elif name == "sort":
            newlist.sort()
        elif name == "pop":
            newlist.pop()
        elif name == "reverse":
            newlist.reverse()
     

