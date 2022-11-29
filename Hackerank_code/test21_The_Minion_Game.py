"""def minion_game(string):
    # your code goes here
    alphabet_vowels = "AEIOUaeiou"
    count = 0
    count2 = 0
    for i in range(len(string)):
        if string[i] in alphabet_vowels:
            for j in range(i,len(string)):
                count += 1
        else:
            for k in range(i,len(string)):
                count2 += 1
    print("Stuart {}".format(count2)) if count2 > count else print("Kevin {}".format(count)) if count > count2 else print("Draw")
"""
def minion_game(string):
    # your code goes here
    alphabet_vowels = "AEIOUaeiou"
    count = 0
    b = 0
    count2 = 0
    d = 0
    count3 = 0
    for i in range(len(string)):
        if string[i] in alphabet_vowels:
            count3 = len(string) - i
            b = count + count3
            count = b
        else:
            count3 = len(string) - i
            count2 = d + count3
            d = count2
    print("Stuart {}".format(count2)) if count2 > count else print("Kevin {}".format(count)) if count > count2 else print("Draw")
if __name__ == '__main__':
    s = "BANANA"
    minion_game(s)