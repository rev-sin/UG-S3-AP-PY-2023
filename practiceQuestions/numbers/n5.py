n = int(input())
sn = str(n)

nn = sn[::-1]

if sn == nn:
    print("palindrome number")
else:
    print("not palindrome number")
