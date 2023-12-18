a = int(input())
b = int(input())

print(f"a is {a}")
print(f"b is {b}")

a, b = b, a
print("after swapping")

print(f"a is {a}")
print(f"b is {b}")
