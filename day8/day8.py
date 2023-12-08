lines = open('input.txt','r').read().splitlines()
prog = lines[0].replace('L','0').replace('R','1')
nodelines = lines[2:]
graph = {l[:3]:(l[l.index('(')+1:l.index(', ')], l[l.index(', ')+2:l.index(')')]) for l in nodelines}

def countsteps(first, last, graph, prog):
    mod = len(prog)
    pc = 0
    cur = first
    while cur != last:
        d = int(prog[pc % mod])
        cur = graph[cur][d]
        pc += 1
    return pc

def pathlimits(firstnodes, lastnodes, graph, prog):
    assert len(firstnodes) == len(lastnodes)
    ids = [i for i in range(len(firstnodes))]
    curnodes = firstnodes.copy()
    endpoints = []
    mod = len(prog)
    pc = 0
    while curnodes:
        d = int(prog[pc%mod])
        for i,n in enumerate(curnodes):
            if int(n.endswith('Z')):
                endpoints.append((firstnodes[ids[i]], n))
                curnodes.pop(i)
                ids.pop(i)
            else:
                curnodes[i] = graph[n][d]
        pc += 1
    return endpoints

print('PART 1 ANSWER:',countsteps('AAA', 'ZZZ', graph, prog))

firstnodes = [l[:3] for l in nodelines if l[:3].endswith('A')]
lastnodes = [l[:3] for l in nodelines if l[:3].endswith('Z')]
limits = pathlimits(firstnodes, lastnodes, graph, prog)
pathlens = [countsteps(lim[0], lim[1], graph, prog) for lim in limits]

from math import lcm
from functools import reduce
n = reduce(lcm, pathlens)
print('PART 2 ANSWER:',n)

'''
PART 2 NOTES

a1 * 11567 = n
a2 * 12643 = n
a3 * 15871 = n
a4 * 16409 = n
a5 * 21251 = n
a6 * 19637 = n

divide by 269

a1 * 43 = n
a2 * 47 = n
a3 * 59 = n
a4 * 61 = n
a5 * 79 = n
a6 * 73 = n

a1 * 43 = a2 * 47 = a3 * 59 = a4 * 61 = a5 * 79 = a6 * 73

exists n such that foreach li in l exists ai such that ai * li == n

we want to find n

we are trying to find the least common multiplier
python can do this dumbass
'''
