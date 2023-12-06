# part 1

with open('input.txt', 'r') as f:
    games = [[g.split(',') for g in l[l.index(':')+1:].strip().split(';')] for l in f.readlines()]

for g in games:
    for i,c in enumerate(g):
        new_c = []
        for x in c:
            x = x.strip().split()
            new_c.append((int(x[0]), x[1]))
        g[i] = new_c

total = 0

for i,g in enumerate(games):
    gid = i + 1
    counters = { 'red': 12, 'green': 13, 'blue': 14, }
    for c in g:
        for x in c:
            if x[0] > counters[x[1]]:
                gid = 0
                break
    total += gid

print("PART 1 ANSWER: ",total)

# part 2

total_power = 0

for g in games:
    powers = { 'red': 0, 'green': 0, 'blue': 0, }
    assert sum(powers.values()) == 0
    for c in g:
        for x in c:
            if x[0] > powers[x[1]]:
                powers[x[1]] = x[0]
    power = 1
    for p in powers.values():
        power *= p
    total_power += power

print("PART 2 ANSWER: ",total_power)

