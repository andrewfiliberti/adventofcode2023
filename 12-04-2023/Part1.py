# Take a seat in the large pile of colorful cards. How many points are they worth in total?
import pandas as pd
import numpy as np
import re

file1 = open('input.txt', 'r')
lines = file1.readlines()

ans = 0

for line in lines:
    game = line.strip().split(":")
    gameNum = game[0].split(" ")[1]
    winNum = re.split(r'\s{1,}', game[1].split("|")[0].strip())
    myNum = re.split(r'\s{1,}', game[1].split("|")[1].strip())
    x = -1
    for n in myNum:
        if n in winNum:
            x += 1
    if x != -1:
        ans += pow(2, x)

print(ans)
    