from math import ceil, floor

with open('input.txt','r') as f:
    data = [[float(x) for x in l[l.find(':')+1:].strip().split()] for l in f.readlines()]

'''
t is the time we hold for
T is the total time

v = t
s = v*(T-t)
s = (T - t)*t = T*t - t^2

s = T*t - t^2
s^-1 = 0.5*(T +/- sqrt(T^2 - 4t))

'''

s = lambda t,T: T*t - t**2
s_inv = lambda s,T: (0.5*(T - (T**2 - 4*s)**0.5), 0.5*(T + (T**2 - 4*s)**0.5))


ways = 1
for i in range(len(data[0])):
    T = data[0][i]
    S = data[1][i]
    tmin = s_inv(S,T)
    tmin = ( tmin[0] + 1 if tmin[0].is_integer() else ceil(tmin[0]) ,
             tmin[1] - 1 if tmin[1].is_integer() else floor(tmin[1])  )
    w = tmin[1] - tmin[0] + 1
    ways *= w

print('PART 1 ANSWER:',ways)

T = float(''.join(str(int(x)) for x in data[0]))
S = float(''.join(str(int(x)) for x in data[1]))

tmin = s_inv(S,T)
tmin = ( tmin[0] + 1 if tmin[0].is_integer() else ceil(tmin[0]) ,
         tmin[1] - 1 if tmin[1].is_integer() else floor(tmin[1])  )
ways = tmin[1] - tmin[0] + 1

print('PART 2 ANSWER:',ways)
