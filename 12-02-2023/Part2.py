# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

import pandas as pd
import numpy as np
import re


file1 = open('input.txt', 'r')
lines = file1.readlines()
ans = 0

for line in lines:
    maxCubes = {"red": 0, "green": 0, "blue": 0}
    newLine = line.split(":")
    game = int(newLine[0].split(" ")[1])
    cubes = re.split('; |, ', newLine[1])
    
    for pull in cubes:
        clean = pull.strip()
        num = int(clean.split(" ")[0])
        color = clean.split(" ")[1]
        
        if maxCubes[color] < num:
            maxCubes[color] = num
    
    power =  maxCubes["red"] * maxCubes["green"] * maxCubes["blue"]
    ans += power
print(ans)
