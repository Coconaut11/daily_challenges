# COMPLETED

#example "([])[]({})" --> true
#example "([}{})" --> false

#Initialize the examples given
data_true = "[][]({})"
data_false = "((()"

def get_result(data):
	# Create a dictionary (aka hashtable) for the 3 diffenert types of brackets we'll have to check.
	to_close = {"(":0, "{":0, "[":0}

	# Loop for every single character
	for i in range(0, len(data)):
		char = data[i]

		# Check which char is, if it opens, we add 1 to the dic, if it closes we substract 1.
		# If we want to close a bracket and another one with different type is already opened, we immediately
		# return False.
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

		# If one of the components of the dic is not 0, it means some of the brackets haven't been closed, so we return False.
		if to_close["("] < 0 or to_close["["] < 0 or to_close["{"] < 0:
			return False

	# If all the components are 0 means all the brackets have been closed, so we return True.
	# If one of them is not 0, we return false as one of them hasn't been closed.
	if to_close["("] == 0 and to_close["["] == 0 and to_close["{"] == 0:
		return True
	else:
		return False

print(get_result(data_false))