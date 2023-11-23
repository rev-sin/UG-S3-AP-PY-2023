l = []
for i in range(1, 101):
    l.append(i)

l.remove(25)

for i in range(1, 101):
    if i not in l:
        print(i)
