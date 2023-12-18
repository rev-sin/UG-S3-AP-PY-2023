def remchar(s1, c1):
    s1 = ''.join(i for i in s1 if i != c1)

    return s1


s = str(input())
c = str(input())
print(remchar(s, c))
