# Including the original set of scratchcards, how many total scratchcards do you end up with?
import pandas as pd
import numpy as np
import re

def addCards(games, x, start, allCards):
    game = start
    count = 0
    while count != x:
        game = game + 1
        allCards.append(game)
        count += 1

    
file1 = open('input.txt', 'r')
lines = file1.readlines()

total = len(lines)
games = {}


for line in lines:
    game = line.strip().split(":")
    gameNum = int(re.split(r'\s{1,}', game[0])[1])
    winNum = re.split(r'\s{1,}', game[1].split("|")[0].strip())
    myNum = re.split(r'\s{1,}', game[1].split("|")[1].strip())

    games[gameNum] = [winNum, myNum]

allCards = list(games.keys())

for key, value in games.items():
    
    w = value[0]
    m = value[1]
    x = 0

    for n in m:
        if n in w:
            x += 1

    if key == 1:
        addCards(games, x, key, allCards)
    else:
        times = allCards.count(key)
        while times != 0:
            if key + x <= total:
                addCards(games, x, key, allCards)
            else:
                addCards(games, total - key, key, allCards)
            times -= 1
    
print(len(allCards))
    
