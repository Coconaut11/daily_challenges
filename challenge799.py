# Solved!

class PrefixMaxSum():
    def __init__(self):
        self.table = {}

    def insert(self, key, val):
        self.table[key] = val

    def sum(self, prefix):
        sum = 0
        for key in self.table.keys():
            if key.startswith(prefix):
                sum += self.table[key]
        return sum

mapsum = PrefixMaxSum()
mapsum.insert("columnar", 3)
print(mapsum.sum("col"))

mapsum.insert("column", 2)
print(mapsum.sum("col"))
