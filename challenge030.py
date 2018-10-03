map = [3, 0, 1, 3, 0, 5]
map2 = [2, 1, 2]

def calc_water(map):
    top = 0
    water = 0
    for i in range(0, len(map)):
        if map[i] < top:
            water += top - map[i]
        else:
            top = map[i]
    return water

print(calc_water(map2))