def count_substring(string, sub_string):
    dem = 0
    for i in range(len(string)):
        x = string.find(sub_string, i, i + len(sub_string))
        if x != -1:
            dem = dem + 1
    return dem

if __name__ == '__main__':
    string = "BANANANANA"
    sub_string = "ANA"
    
    count = count_substring(string, sub_string)
    print(count)

"""def count_substring(string, sub_string):
    count = 0
    for _ in range(len(string)):
        if string[_:_ + len(sub_string)] == sub_string:
            count += 1    
        
    return count"""
