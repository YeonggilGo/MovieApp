from functools import reduce

keys = [3, 2, 1]
user_prefer = {
    1: [18, 53],
    2: [28, 33],
    3: [11, 3],
}
for i in range(1, len(keys)):
    print(i, reduce(lambda x, m: x + m, [user_prefer[j] for j in keys[:i]], []), sep=':')
