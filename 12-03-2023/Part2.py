# Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
import pandas as pd
import numpy as np
import re

def getSymbol(matrix, numbers):
    s = {}
    g = 1
    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if matrix[x][y] == "*":
                s[g] = [x,y]
                g += 1
    return s


def createMatrix():
    file1 = open('input.txt', 'r')
    lines = file1.readlines()
    matrix = []
    
    for line in lines:
        l = []
        for char in line.strip():
            l.append(char)
        matrix.append(l)
    return matrix

# example: if ind = [3,4], we need to check left: [3,3], right: [3,5], up: [2,4], down: [4. 4] upleft: [2,3], upright: [2,5], downleft: [4,3], downright: [4,5]

def checkSym(ind, matrix, symbols):
    x = int(ind[0])
    y = int(ind[1])
    possible = [[x, y-1], [x, y+1], [x-1, y], [x+1, y], [x-1, y-1], [x-1, y+1], [x+1, y-1], [x+1, y+1]]
    clean = []
    for p in possible:
        if p[0] < 0 or p[0] >= len(matrix) or p[1] < 0 or p[1] > len(matrix[0]):
            continue
        else:
            clean.append(p)
    k = []
    for key, val in symbols.items():
        if val in clean:
            k.append(key)
    return k
        
numbers = '1234567890'

matrix = createMatrix()
symbols = getSymbol(matrix, numbers)
i = 0
matches = {}

while i != len(matrix):
    num = ""
    flag = []
    for j in range(len(matrix[i])):
        if matrix[i][j] in numbers:
            num += matrix[i][j]
            flag.append(checkSym([i,j], matrix, symbols))
            if j == len(matrix[i]) - 1:
                flat_list = set([item for sublist in flag for item in sublist])
                for gear in flat_list:
                    if gear in matches:
                        matches[gear].append(int(num))
                    else:
                        matches[gear] = [int(num)]
                flat_list = None
                num = ""
                flag = []
        else:
            flat_list = set([item for sublist in flag for item in sublist])
            for gear in flat_list:
                if gear in matches:
                    matches[gear].append(int(num))
                else:
                    matches[gear] = [int(num)]
            num = ""
            flag = []
    i += 1
ans = 0
for key, val in matches.items():
    if len(val) == 2:
        prod = val[0] * val[1]
        ans += prod
        
print(ans)
        