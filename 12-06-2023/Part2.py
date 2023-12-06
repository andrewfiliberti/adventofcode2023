# Including the original set of scratchcards, how many total scratchcards do you end up with?
import pandas as pd
import numpy as np
import re

    
file1 = open('input.txt', 'r')
lines = file1.readlines()

time = int("".join(re.split(r'\s{1,}', lines[0].split(":")[1].strip())))
record = int("".join(re.split(r'\s{1,}', lines[1].split(":")[1].strip())))

ans = 0

for n in range(1, time + 1):
    dist = n * (time - n)
    if dist > record:
        ans += 1

print(ans)