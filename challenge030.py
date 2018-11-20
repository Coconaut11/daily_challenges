map = [3, 0, 1, 3, 0, 5]
map2 = [2, 1, 2]

def calc_water(map):
    top = 0
    water = 0
    for i in range(len(map)):
        if map[i] < top:
            water += top - map[i]
        else:
            top = map[i]
    return water

def draw_map(map):
    width = len(map)
    height = max(map)
    for h in reversed(range(height+2)): #2 to add a line at the beginning.
        line = ""
        for x in range(width):
            if map[x] >= h:
                line += "H "
            else:
                line += "  "
        print(line)

draw_map(map)
print(calc_water(map))