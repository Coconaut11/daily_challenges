# COMPLETED

data = "The quick brown fox jumps over the lazy dog. And fucks your mother, who's a bitch. Your father is a very good man though, he works day and night to pay your bills, which you should be grateful for. Ok, I stop, bye. I hope we meet again soon and you suck my dick once again."

def get_result(data, k):
    result = []
    current_line = ""
    for i in range(0, len(data)):
        if len(current_line) + len(data[i])+1 > k:
            result.append(justify(current_line, k))
            current_line = data[i] + " "
        else:
            current_line += data[i] + " "
    print(current_line)
    if current_line != "":
        result.append(current_line)

def justify(line, k):
    _line = line.split()
    for i in range(0, len(_line)-1):
        _line[i] += " "

    gaps = len(_line)-1
    spaces = k - (len(line))

    res = ""

    while spaces > 0:
        for i in range(0, gaps):
            if spaces > 0:
                _line[i] += " "
                spaces -= 1

    for i in range(0, len(_line)):
        res += _line[i]

    print(res)
    return res

print(" ")
get_result(data.split(), 50)