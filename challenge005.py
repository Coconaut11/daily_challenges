#COMPLETED

def createPair(a, b):
    return [a, b]

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair(createPair)

def car(cons):
    return cons[0]

def cdr(cons):
    return cons[1]

print(car(cons(3, 4)))
print(cdr(cons(3, 4)))
