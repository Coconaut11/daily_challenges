import os

def render(w, h):
    os.system("cls")
    for y in range(h):
        line = ""
        for x in range(w):
            line += "0 "
        print(line)
        print("caca")
render(10, 10)