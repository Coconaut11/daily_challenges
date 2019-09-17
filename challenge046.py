# COMPLETED :d

from collections import namedtuple
struct = namedtuple

data = "banana"
data = "asjdflkdsjfasdffdsaalksjdflk"

Palindrom = struct("Pal", "len start end")

def get_longest_palindrom(data):
	hi = Palindrom(0, 0, 0)

	for i in range(len(data)):
		a = data[i]
		for j in range(i+1, len(data)):
			if hi.len < j-i:
				b = data[j]
				if a == b:
					if(check_palindrom(substring(data, i, j)) == True):
						hi = Palindrom(j-i, i, j)

	print("Found highest palindrom: ")
	print(substring(data, hi.start, hi.end))

def check_palindrom(sub):
	if len(sub) == 1:
		return True

	if len(sub) == 2:
		if sub[0] == sub[1]:
			return True
		else:
			return False

	if sub[1] == sub[len(sub)-2]:
		return check_palindrom(substring(sub, 1, len(sub)-2))
	else:
		return False

def substring(s, i0, i1):
    s = s[i0 : i0 + i1-i0+1]
    return s


get_longest_palindrom(data);