#COMPLETED - Can be better...

data = [10, 15, 3, 7, 2, 5, 6, 7, 2, 4]

def check_sum(data, k):
    seen = [0]
    for i in range(0, len(data)):
        for j in range(0, len(seen)):
            if(data[i] == seen[j]):
                return True
            seen += [k - data[i]]
    return False

print(check_sum(data, 25))
