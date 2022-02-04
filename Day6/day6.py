from collections import defaultdict, Counter

lantern_fish = Counter([int(x) for x in open('day6.txt').read().split(',')])


for x in range(256):
    counts = defaultdict(int)
    for k, v in lantern_fish.items():
        if k == 0:
            counts[6] += v
            counts[8] += v
        else:
            counts[k-1] += v
    lantern_fish = counts
    if x == 79:
        print(sum(lantern_fish.values()))
print(sum(lantern_fish.values()))

        

