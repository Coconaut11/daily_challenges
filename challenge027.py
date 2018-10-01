# COMPLETED

#example "([])[]({})" --> true
#example "([}{})" --> false

data_true = "[][]({})"
data_false = "((()"

def get_result(data):
	to_close = {"(":0, "{":0, "[":0}
	for i in range(0, len(data)):
		char = data[i]
		if char == "(":
			to_close["("] = to_close["("] + 1
		elif char == ")":
			if to_close["{"] != 0 or to_close["["] != 0:
				return False
			to_close["("] = to_close["("] - 1
		elif char == "{":
			to_close["{"] = to_close["{"] + 1
		elif char == "}":
			if to_close["("] != 0 or to_close["["] != 0:
				return False
			to_close["{"] = to_close["{"] - 1
		elif char == "[":
			to_close["["] = to_close["["] + 1
		elif char == "]":
			if to_close["{"] != 0 or to_close["("] != 0:
				return False
			to_close["["] = to_close["["] - 1

		print(to_close)

		if to_close["("] < 0 or to_close["["] < 0 or to_close["{"] < 0:
			return False

	if to_close["("] == 0 and to_close["["] == 0 and to_close["{"] == 0:
		return True
	else:
		return False

print(get_result(data_false))