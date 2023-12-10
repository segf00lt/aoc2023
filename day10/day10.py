data = open('input.txt','r').read().splitlines()

def getsteps(start, cur):
    pipetab = {
            '|': [ (1, 0),  (0, 0) ],
            '-': [ (0, 0),  (0, 1) ],
            'L': [ (0, 1),  (1, 0) ],
            'J': [ (0,-1),  (-1,0) ],
            '7': [ (0, 1),  (1, 0) ],
            'F': [ (0,-1),  (-1,0) ],
            }
    prev = start
    steps = []
    positions = [cur]
    i = 1
    while cur != start:
        c = data[cur[0]][cur[1]]
        if c == '.':
            breakpoint()
        orient = 0 if cur[0] != prev[0] else 1
        direct = cur[orient] - prev[orient]
        prev = cur
        cur = (cur[0] + pipetab[c][orient][0]*direct, cur[1] + pipetab[c][orient][1]*direct)
        steps.append(i)
        positions.append(cur)
        i += 1
    return steps, positions

start = (90, 62)
#start = (4,12)

cur = (90, 63)
#cur = (4,13)
steps1, positions1 = getsteps(start, cur)

cur = (89, 62)
#cur = (5,12)
steps2, positions2 = getsteps(start, cur)

far = 0
for a,b in zip(steps1, reversed(steps2)):
    if a == b:
        far = a

print('PART 1 ANSWER:',far)

from matplotlib.path import Path

p = Path(positions1)
count = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if (i, j) in positions1:
            continue
        if p.contains_point((i, j)):
            count += 1

print('PART 1 ANSWER:',count)
