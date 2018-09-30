# COMPLETED

data = [10, 5, 2, 7, 8, 7]

def get_result(data):
	result = [0]*(len(data)-2)
	for i in range(0, len(data)-2):
		high = data[i]
		if(data[i+1] > high):
			high = data[i+1]
		if(data[i+2] > high):
			high = data[i+2]
		result[i] = high
	return result

print(get_result(data))