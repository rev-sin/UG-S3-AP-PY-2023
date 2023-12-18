l1 = [1, 2, 3, 4, 5, 6]
pairs = []
s = set()

n = 7

for i in l1:
    c = n - i
    if c in s:
        pairs.append((i, c))
    s.add(i)

print(pairs)
