# Including the original set of scratchcards, how many total scratchcards do you end up with?
import pandas as pd
import numpy as np
import re

    
file1 = open('input.txt', 'r')
lines = file1.readlines()

time_list = re.split(r'\s{1,}', lines[0].split(":")[1].strip())
rec_list = re.split(r'\s{1,}', lines[1].split(":")[1].strip())

ways = []

for i, time in enumerate(time_list):
    t = int(time)
    w = 0
    for n in range(1, t + 1):
        dist = n * (t - n)
        if dist > int(rec_list[i]):
            w += 1
    ways.append(w)

ans = 1
for x in ways:
    ans = ans * x
    
print(ans)