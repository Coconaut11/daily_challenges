#COMPLETED*

data = "12345"

def decoder(data, k):
    if k <= 0:
        return 1

    result = decoder(data, k-1)
    off = len(data)-k
    if k > 1 and int(data[0+off] + data[1+off]) <= 26:
        result = result + decoder(data, k-2)
    return result

def decode_ways(data):
    return decoder(data, len(data))

print("Result: " + str(decode_ways(data)))