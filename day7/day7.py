kinds = [
		(5,1,1),
		(4,1,2),
		(3,1,2),
		(3,1,3),
		(2,2,3),
		(2,1,4),
        (1,5,5),
        ]

def card_cmp(a, b):
    # this was not the first version of this comparison function LOL
    ltoi = {l:i for i,l in enumerate('23456789TJQKA')}
    da = {x:a.count(x) for x in a}
    db = {x:b.count(x) for x in b}
    vda = da.values()
    vdb = db.values()
    akind = (len(da), min(vda), max(vda))
    bkind = (len(db), min(vdb), max(vdb))
    if akind == bkind:
        for x in list(zip(a,b)):
            if x[0] != x[1]:
                return ltoi[x[0]] - ltoi[x[1]]
    else:
        return (kinds.index(akind)+1) - (kinds.index(bkind)+1)

def card_J_cmp(a, b):
    ltoi = {l:i for i,l in enumerate('J23456789TQKA')}
    anoJ = a.replace('J','')
    da = {x:anoJ.count(x) for x in anoJ}
    if da:
        most = sorted(da.items(),key=lambda x:x[1], reverse=True)[0][0]
        da[most] += list(a).count('J')
    else: da = {'J':len(a)}
    bnoJ = b.replace('J','')
    db = {x:bnoJ.count(x) for x in bnoJ}
    if db:
        most = sorted(db.items(),key=lambda x:x[1], reverse=True)[0][0]
        db[most] += list(b).count('J')
    else: db = {'J':len(b)}
    vda = da.values()
    vdb = db.values()
    akind = (len(da), min(vda), max(vda))
    bkind = (len(db), min(vdb), max(vdb))
    if akind == bkind:
        for x in list(zip(a,b)):
            if x[0] != x[1]:
                return ltoi[x[0]] - ltoi[x[1]]
    else:
        return (kinds.index(akind)+1) - (kinds.index(bkind)+1)

class Card:
    # I hate how the python sorting methods work
    def __init__(self, card, score, cmp):
        self.card = card
        self.score = score
        self.cmp = cmp
    def __eq__(self, other):
        return self.cmp(self.card, other.card) == 0
    def __ne__(self, other):
        return self.cmp(self.card, other.card) != 0
    def __lt__(self, other):
        return self.cmp(self.card, other.card) < 0
    def __le__(self, other):
        return self.cmp(self.card, other.card) <= 0
    def __gt__(self, other):
        return self.cmp(self.card, other.card) > 0
    def __ge__(self, other):
        return self.cmp(self.card, other.card) >= 0
    def __repr__(self):
        return f"(card={self.card}, score={self.score})"

with open('input.txt','r') as f:
    hands = [[x if i==0 else int(x) for i,x in enumerate(l.strip().split())] for l in f.readlines()]

hands = [Card(x[0],x[1],card_cmp) for x in hands]

print('PART 1 ANSWER:',sum(c.score*(i+1) for i,c in enumerate(sorted(hands))))

for c in hands:
    c.cmp = card_J_cmp

print('PART 2 ANSWER:',sum(c.score*(i+1) for i,c in enumerate(sorted(hands))))
