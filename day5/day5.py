import re

DEBUG = False

with open('input.txt','r') as f:
    data = f.read()

par = [p[p.find('\n')+1:].strip() for p in re.split(r'\n\s*\n', data)]
map_names = [p[:p.find(':')].strip() for p in re.split(r'\n\s*\n', data)][1:]
seeds = [int(x) for x in par[0].split(' ')[1:]]

maps = []

for p in par[1:]:
    mat = [[int(x) for x in l.split()] for l in p.splitlines()]
    maps.append(mat)

location = []
for s in seeds:
    cur = s
    for m in maps:
        mapped = -1
        for i,r in enumerate(m):
            if r[1] <= cur <= r[1]+r[2]:
                mapped = i
        if mapped != -1:
            cur = m[mapped][0] + cur - m[mapped][1]
    location.append(cur)

print('PART 1 ANSWER:',min(location))

seed_ranges = [(seeds[i],seeds[i]+seeds[i+1]) for i in range(0,len(seeds),2)]
if DEBUG: print('seeds as ranges =',seed_ranges)
next_seed_ranges = []
for mi,m in enumerate(maps):
    if DEBUG: print('currently at',map_names[mi])
    tmp = None
    for sri,sr in enumerate(seed_ranges):
        mapped_ranges = []
        for i,r in enumerate(m):
            src = r[1]
            end = r[1]+r[2]
            dest = r[0]
            if sr[0] >= src and sr[1] <= end: # sr is totally inside the map
                mapped_ranges.append(((sr[0] - src) + dest, (sr[1] - src) + dest))
                break
            elif sr[0] < src and sr[1] > end: # the map is totally inside sr
                mapped_ranges.append((dest, (end - src) + dest))
            # partial overlaps
            if sr[0] >= src and sr[0] < end:
                mapped_ranges.append(((sr[0] - src) + dest, (end - src) + dest))
            elif sr[1] >= src and sr[1] <= end:
                mapped_ranges.append((dest, (sr[1] - src) + dest))
        if mapped_ranges:
            next_seed_ranges += mapped_ranges
            if DEBUG: print('seed',sr,'mapped to',mapped_ranges)
        else:
            next_seed_ranges.append(sr)
            if DEBUG: print('seed',sr,'mapped to',sr)
    tmp = seed_ranges
    seed_ranges = next_seed_ranges
    tmp.clear()
    next_seed_ranges = tmp
    if DEBUG:
        print()
        print('after',map_names[mi],'=',seed_ranges)
                
print('PART 2 ANSWER:',min(seed_ranges)[0])

