levels = [int(x) for x in open('day1.txt').readlines()]

total = 0 
for x in range(len(levels) - 1):
    if levels[x+1] > levels[x]:
        total += 1

total2 = 0
for x in range(len(levels) - 3):
    if levels[x] < levels[x+3]:
        total2 += 1

print(total)
print(total2)