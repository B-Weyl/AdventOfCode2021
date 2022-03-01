caves = [x.strip() for x in open('day9.txt').readlines()]

total_risk = 0
low_points = set()


# part 1

# rows
for x in range(len(caves)):
    # a single points list of neighbors
    neighbors = []
    #columns
    for y in range(len(caves[0])):
        if x > 0:
            neighbors.append(caves[x-1][y])
        if x < len(caves) - 1:
            neighbors.append(caves[x+1][y])
        if y > 0:
            neighbors.append(caves[x][y-1])
        if y < len(caves[0]) - 1:
            neighbors.append(caves[x][y+1])
        if caves[x][y] < min(neighbors):
            total_risk += int(caves[x][y]) + 1
            low_points.add((x, y))
        # reset neighbors list for the next point in the grid.
        neighbors = []
print(total_risk)

# part 2    




            






            


    
