import random

def create_sudoku(n):
    full = [[0 for x in range(9)] for y in range(9)]
    data = [[0 for x in range(9)] for y in range(9)]

    #Create a full solved sudoku
    for i in range(n):
        x = random.randint(0, 8)
        y = random.randint(0, 8)
        while full[x][y] != 0:
            x = random.randint(0, 8)
            y = random.randint(0, 8)
        print("(" + str(x) + ", " + str(y) + ")")
        cont = True
        while cont:
            cont = False
            n = random.randint(1, 9)
            for xx in range(9):
                if full[xx][y] == n:
                    cont = True
            for yy in range(9):
                if full[x][yy] == n:
                    cont = True
        print("(" + str(x) + ", " + str(y) + "): " + str(n))
        full[x][y] = n

    return full
    
def print_sudoku(data):
    for y in range(9):
        to_print = ""
        for x in range(9):
            extra_space = ""
            if (x+1) % 3 == 0:
                extra_space = " "
            to_print += str(data[x][y]) + " " + extra_space
        print(to_print)
        if (y+1) % 3 == 0:
            print("")

def solve_sudoku(data):
    pass

data = create_sudoku(random.randint(27, 35))
print_sudoku(data)
solve_sudoku(data)