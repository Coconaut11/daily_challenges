#COMPLETED

data = "AAAABBBCCDAA"

def encode(data):
	count = 0
	res = ""
	char = None
	for i in range(0, len(data)):
		if i == 0:
			char = data[0]
			count = 1
			continue

		if char == data[i]:
			count += 1
		else:
			res += (str(count) + char)
			char = data[i]
			count = 1

		if i == len(data)-1:
			res += (str(count) + char)

	return res

def decode(data):
	res = ""
	for i in range(0, int(len(data)/2)):
		count = int(data[i*2])
		char = data[i*2+1]
		for i in range(0, count):
			res += char
	return res

print(encode(data))
print(decode(encode(data)))