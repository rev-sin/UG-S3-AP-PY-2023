l1 = []

for i in range(1, 101):
    l1.append(i)

m = int(input())

if m not in l1:
    print("not in list")
else:
    print("in list")
