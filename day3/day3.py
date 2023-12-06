# part 1

import re

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

partsum = 0

for i,l in enumerate(data):
    numbers = re.finditer(r'\d+', l)
    indices = [(match.start(), match.end()) for match in numbers]
    for ind in indices:
        b = 0 if ind[0] == 0 else 1
        e = 0 if ind[1] == len(l) else 1
        look = ''.join([l[ind[0]-b:ind[1]+e], data[(i-1)%len(data)][ind[0]-b:ind[1]+e], data[(i+1)%len(data)][ind[0]-b:ind[1]+e]])
        look = re.sub(r'[0-9.]', '', look)
        if look:
            partsum += int(l[ind[0]:ind[1]])

print('PART 1 ANSWER:',partsum)

gearsum = 0

# consider all intervals to be inclusive
for i,l in enumerate(data):
    tmp = re.finditer(r'\*', l)
    stars = [(m.start() - (1 if m.start() > 0 else 0), m.start() + (1 if m.start() < len(l)-1 else 0)) for m in tmp]
    same = l
    above = data[i-(1 if i > 0 else 0)]
    below = data[i+(1 if i < len(data)-1 else 0)]
    tmp = [re.finditer(r'\d+', same),
            re.finditer(r'\d+', above),
            re.finditer(r'\d+', below)]
    nums = [[(match.start(), match.end()-1) for match in row] for row in tmp]
    overlap = lambda t1, t2: not (t1[1] < t2[0] or t1[0] > t2[1])
    for s in stars:
        ratio = 1
        gears = [int(same[n[0]:n[1]+1]) for n in nums[0] if overlap(n, s)] + [int(above[n[0]:n[1]+1]) for n in nums[1] if overlap(n, s)] + [int(below[n[0]:n[1]+1]) for n in nums[2] if overlap(n, s)]
        if len(gears) < 2:
            continue
        for g in gears:
            ratio *= g
        gearsum += ratio

print('PART 2 ANSWER:',gearsum)
