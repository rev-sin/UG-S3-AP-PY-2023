d = {10: 'a',
     20: 'b',
     30: 'c'}

d[40] = 'd'

for i in d.values():
    print(i)

for i, j in d.items():
    print(i, j)
