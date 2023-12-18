s = str(input())
ch = str(input())
c = 0

for i in s:
    if i == ch:
        c += 1

print(f"{ch} occurs {c} times")
