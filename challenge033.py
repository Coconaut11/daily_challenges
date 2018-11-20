data = [2, 1, 5, 7, 2, 0, 5]

def print_running_med(data):
    sum = 0
    for i in range(0, len(data)):
        sum += data[i]
        med = sum/(i+1)
        print(med)

print_running_med(data)