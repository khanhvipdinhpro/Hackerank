if __name__ == '__main__':
    def a(x):
        return x.isalnum()
    def b(x):
        return x.isalpha()
    def c(x):
        return x.isdigit()
    def d(x):
        return x.islower()
    def e(x):
        return x.isupper()
    s = input()
    print(any(list(map(a, s))))
    print(any(list(map(b, s))))
    print(any(list(map(c, s))))
    print(any(list(map(d, s))))
    print(any(list(map(e, s))))
    """print(any(list(map(lambda x: x.isalnum(), s))))
    print(any(list(map(lambda x: x.isalpha(), s))))
    print(any(list(map(lambda x: x.isdigit(), s))))
    print(any(list(map(lambda x: x.islower(), s))))
    print(any(list(map(lambda x: x.isupper(), s))))
    """