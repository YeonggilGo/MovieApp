from functools import reduce

a = {1: [1, 2, 3], 2: [4, 5, 6]}
print(list(a.values()))
print(reduce(lambda x, m: x + m, list(a.values()), []))
