data = [6, 1, 3, 3, 3, 6, 6] #return 1
data2 = [13, 19, 13, 13] #return 19

def get_result(data):
    seen = {}
    for i in range(len(data)):
        if