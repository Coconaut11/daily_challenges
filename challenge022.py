data_00 = {"quick":"yas", "brown":"yas", "the":"yas", "fox":"yas"}
data_01 = "thequickbrownfox"

def get_result(data_00, data_01):
	res = ""
	idx = 0
	leng = 0
	used = 0
	while idx < len(data_01):
		s = substring(data_01, idx, idx+leng)
		if data_00.get(s, None) is not None:
			res = str(res) + str(s) + " "
			used += 1
			idx = idx + leng + 1
			leng = 0	
		else:
			leng += 1		

	if used == len(data_00):
		return res
	else:
		return None

def substring(s, i0, i1):
    s = s[i0 : i0 + i1-i0+1]
    return s

print(get_result(data_00, data_01))