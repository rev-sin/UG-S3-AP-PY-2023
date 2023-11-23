l = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 8, 5, 6, 7, 8]

l = [1, 2, 3, 4, 5, 6, 7, 8]# l = [1, 2, 3, 4, 5, 6, 7, 8]
s = set(l)

if l != list(s):
    print("There are duplicates!")
