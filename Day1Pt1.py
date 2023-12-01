import pandas as pd
import numpy as np


file1 = open('input.txt', 'r')
lines = file1.readlines()

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ans = 0

for line in lines:
    l = []
    print(line)
    for char in line:
        if char not in alphabet and char != "\n":
            l.append(char)
    num = (int(l[0]) * 10) + int(l[-1])
    ans += num
    print(num)

print(ans)