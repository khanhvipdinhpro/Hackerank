def merge_the_tools(string, k):
    # your code goes here
    
    for i in range(0,len(string),k):
        my_list = string[i:i+k]
        my_list2 = ""
        for j in range(len(my_list)):
            x = my_list[j+1:len(my_list)].find(my_list[j])
            y = my_list2.find(my_list[j])
            if x == -1 and y == -1:
                my_list2 = my_list2 + my_list[j]
            elif x != -1 and y == -1:
                my_list2 = my_list2 + my_list[j]
            elif x != -1 and y != -1:
                my_list2 = my_list2
        print(my_list2)


if __name__ == '__main__':
    string, k = "AABCAAADA", 3
    merge_the_tools(string, k)

"""count_chr = my_list.count(my_list[j])
print(count_chr)
my_list2 = my_list[::-1]
my_list3 = my_list2.replace(my_list[j],"",count_chr-1)
my_list4 = my_list3[::-1]"""