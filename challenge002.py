#COMPLETED - Can surely be better

data = [3, 2, 1]

def getResult(data):
	result = [0] * len(data)
	for i in range(0, len(data)):
		mul = 1
		for j in range(0, len(data)):
			if i != j:
				mul = mul * data[j]
		result[i] = mul
	return result

print(getResult(data))