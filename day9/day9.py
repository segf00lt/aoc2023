hists = [list(map(int, l.split())) for l in open('input.txt','r').read().splitlines()]
piles = []

for hist in hists:
    pile = [hist]
    i = 0
    while True:
        hnew = []
        h = pile[i]
        for j in range(len(h)-1):
            hnew.append(h[j+1] - h[j])
        if sum(hnew) == 0:
            break
        pile.append(hnew)
        i += 1
    i = len(pile)-1
    while i > 0:
        pile[i-1].append(pile[i-1][-1] + pile[i][-1])
        i -= 1
    piles.append(pile)

print('PART 1 ANSWER:',sum([h[-1] for h in hists]))

total = 0
for pile in piles:
    pile[-1].insert(0,pile[-1][0])
    i = len(pile)-1
    while i > 0:
        pile[i-1].insert(0, pile[i-1][0] - pile[i][0])
        i -= 1
    total += pile[0][0]

print('PART 2 ANSWER:',total)
