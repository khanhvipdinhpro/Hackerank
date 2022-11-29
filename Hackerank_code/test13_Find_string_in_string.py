def count_substring(string, sub_string):
    dem = 0
    for i in range(len(string)):
        x = string.find(sub_string, i, i + len(sub_string))
        if x != -1:
            dem = dem + 1
    return dem

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)