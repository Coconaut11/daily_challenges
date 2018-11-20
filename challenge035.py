data = ["G", "B", "R", "R", "B", "R", "G"]

def sort(data):
    res = []
    end_R = 0
    for i in range(len(data)):
        if data[i] == "R":
            res.insert(0, "R")
            end_R += 1
        elif data[i] == "G":
            res.insert(end_R, "G")
        elif data[i] == "B":
            res.append("B")
        else:
            return ["Error :D"]

    return res

print(sort(data))