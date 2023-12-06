with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

total = 0

for l in lines:
    digits = [d for d in l if d in '0123456789']
    total += int(f"{digits[0]}{digits[-1]}")

print(total)
