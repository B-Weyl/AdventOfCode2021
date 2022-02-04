from collections import defaultdict 

part2 = True

pts1 = defaultdict(int)
pts2 = defaultdict(int)
with open('day5.txt') as f:
    for l in f:
        p1, p2 = l.split(" -> ")
        x1, y1 = [int(x) for x in p1.split(',')]
        x2, y2 = [int(x) for x in p2.split(',')]

        if x1 == x2:
            if y1 < y2:
                for y in range(y1, y2 + 1):
                    pts1[(x1, y)] += 1
                    pts2[(x1, y)] += 1
            else:
                for y in range(y2, y1 + 1):
                    pts1[(x1, y)] += 1
                    pts2[(x1, y)] += 1
        elif y1 == y2:
            if x1 < x2:
                for x in range(x1, x2 + 1):
                    pts1[(x, y1)] += 1
                    pts2[(x, y1)] += 1
            else:
                for x in range(x2, x1 + 1):
                    pts1[(x, y1)] += 1
                    pts2[(x, y1)] += 1
        elif part2:
            if x1 > x2:
                dx = -1
            else:
                dx = 1
            if y1 > y2:
                dy = -1
            else:
                dy = 1
            x = x1
            y = y1
            while x != x2 and y != y2:
                pts2[(x, y)] += 1
                x += dx
                y += dy
            pts2[(x, y)] += 1
intersects1, intersects2 = 0, 0
for pt, n in pts1.items():
    if n >= 2:
        intersects1 += 1

for pt, n in pts2.items():
    if n >= 2:
        intersects2 += 1
print(intersects1, intersects2)


