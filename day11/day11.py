import numpy as np
from itertools import combinations

data = [[0 if col == '.' else 1 for col in row] for row in open('input.txt','r').read().splitlines()]
space = np.array(data)
del data

ones = np.where(space == 1)
galaxies = list(zip(ones[0], ones[1]))
pairs = list(combinations(galaxies, 2))

def distance(a, b, inc):
    yexpansion = 0
    start = min(a[0], b[0])
    end = max(a[0], b[0])
    for idx in range(start, end):
        if np.sum(space[idx]) == 0:
            yexpansion += inc
    xexpansion = 0
    start = min(a[1], b[1])
    end = max(a[1], b[1])
    for idx in range(start, end):
        if np.sum(space[:,idx]) == 0:
            yexpansion += inc
    return abs(b[0] - a[0] + yexpansion) + abs(b[1] - a[1] + xexpansion)

total_1 = 0
total_2 = 0
for pair in pairs:
    total_1 += distance(pair[0], pair[1], 1)
    total_2 += distance(pair[0], pair[1], 999999)
print('PART 1 ANSWER:',total_1)
print('PART 2 ANSWER:',total_2)
