directions = open('day2.txt').readlines()


x, depth, aim = 0, 0, 0
x2, depth2 = 0, 0


for d in directions:
    cmd, amt = d.split(' ')

    match cmd:
        case 'forward':
            x += int(amt)
        case 'down':
            depth += int(amt)
        case 'up':
            depth -= int(amt)

for d in directions:
    cmd, amt = d.split(' ')

    match cmd:
        case 'forward':
            x2 += int(amt)
            depth2 += aim * int(amt)
        case 'down':
            aim += int(amt)
        case 'up':
            aim -= int(amt)


    
print(depth * x)
print(depth2 * x2)

