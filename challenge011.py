#COMPLETED - Not efficient enough but.. fuck it..

data = ["dog", "deer", "deal"]

def query(data, k):
    result = []
    for x in data:
        if x.startswith(k):
            result = result + [x]
    return result

print(query(data, "de"))