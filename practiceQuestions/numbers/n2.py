n = int(input())
sn = str(n)
sum1 = 0

for i in sn:
    sum1 += int(i) ** len(sn)

if sum1 == n:
    print("is armstrong number")
else:
    print("not armstrong number")
