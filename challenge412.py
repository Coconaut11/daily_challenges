def get_term(prev_term):
    str_term = str(prev_term)
    res = ""
    count = 1
    for i in range(len(str_term)):
        it = str_term[i]
        next_it = ""
        if i == len(str_term)-1:
            res += str(count) + str_term[i]
            continue
        next_it = str_term[i+1]
        if it == next_it:
            count += 1
        else:
            res += str(count) + it
            count = 1
            
    return int(res)

def test():
    print(get_term(21))

def main():
    n = 20
    term = 1
    for i in range(n):
        print(term)
        term = get_term(term)
    print(term)

main()