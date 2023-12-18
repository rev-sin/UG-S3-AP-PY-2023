n = int(input())
sn = str(n)
b = True

for i in sn:
    if i not in ('0', '1'):
        b = False

if b:
    print("binary number")
else:
    print("not binary number")
