import pandas as pd
import numpy as np


file1 = open('input.txt', 'r')
lines = file1.readlines()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
words = {'one': "o1ne", 'two': "t2wo", 'three': "th3ree", 'four': "f4our", 'five': "f5ive", 'six': "s6ix", 'seven': "se7ven", 'eight': "e8ight", 'nine': "ni9ne"}
ans = 0

for line in lines:
    l = []
    print(line)
    for key, value in words.items():
        line = line.replace(key, value)
    for char in line:
        if char not in alphabet and char != "\n":
            l.append(char)
    num = (int(l[0]) * 10) + int(l[-1])
    ans += num
    print(num)

print(ans)
