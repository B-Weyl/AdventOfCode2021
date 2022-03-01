import numpy as np

# levels = list([x.split() for x in open('day11.txt').readlines()])
levels = open('day11test.txt').read().split('\n')
grid = []
for line in open('day11.txt'):
    grid.append([int(x) for x in line.strip()])


FLASHES = 0

def flash(x, y):
    global FLASHES
    FLASHES += 1
    grid[x][y] = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            xx = x+dx
            yy = y+dy
            if 0<=xx<len(grid) and 0<=yy<len(grid[0]) and grid[xx][yy] != 0:
                grid[xx][yy] += 1
                if grid[xx][yy] >= 10:
                    flash(xx, yy)


t = 0
while True:
    t += 1
# for a in range(100):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] += 1
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 10:
                flash(x, y)
    done = True
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 0:
                continue
            else:
                done = False
    if t == 100:
        print(FLASHES)
    if done:
        print(t)
        break

# guessed : 1615

    



        
        
        
