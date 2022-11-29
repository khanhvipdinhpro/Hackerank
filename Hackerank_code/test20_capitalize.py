import math
import os
import random
import re
import sys

def solve(s):
    my_name = list(map(lambda x : x.capitalize(), s.split(" ")))
    upcase_name = " ".join(my_name)
    return upcase_name

print(solve("khanh   nguyen haha"))