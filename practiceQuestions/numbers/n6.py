a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c:
    print(f"{a} is greatest")
elif b >= a and b >= c:
    print(f"{b} is greatest")
else:
    print(f"{c} is greatest")
