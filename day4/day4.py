# part 1

with open('input.txt','r') as f:
    lines = [l[l.index(':')+1:] for l in f.readlines()]
    cards = [([int(x) for x in l[:l.index('|')].strip().split()], [int(x) for x in l[l.index('|')+1:].strip().split()]) for l in lines]

points = 0
wins = []

for c in cards:
    win = list(set(c[0]) & set(c[1]))
    wins.append(len(win))
    p = len(win) - 1
    if p >= 0:
        points += 1 << p

print('PART 1 ANSWER:', points)

# part 2

cardnums = [i for i in range(len(cards))]

for i,n in enumerate(cardnums):
    win = wins[n]
    copies = cardnums[cardnums[i]+1:cardnums[i]+win+1]
    cardnums += copies

print('PART 2 ANSWER:', len(cardnums))
