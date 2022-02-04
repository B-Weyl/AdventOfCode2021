positions = [int(x) for x in open('day7.txt').read().split(',')]
max_position = max(positions)


totals = {}
totals2 = {}

def cost(number):
    return number * (number + 1) // 2


for x in range(max_position):
    fuel = 0
    for p in positions:
        fuel += abs(x - p)
    totals[x] = fuel
print(min(totals.values()))
# to see what position they align to
for k, v in totals.items():
    if v == min(totals.values()):
        print(k, v)


# part 2
for x in range(max_position):
    fuel = 0
    for p in positions:
        fuel += cost(abs(x - p))
    totals2[x] = fuel

for k, v in totals2.items():
    if v == min(totals2.values()):
        print(k, v)
print(min(totals2.values()))