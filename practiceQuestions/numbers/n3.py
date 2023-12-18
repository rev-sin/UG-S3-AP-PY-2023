n = int(input())

if n < 2:
    print("invalid")

elif n == 2:
    print("prime number")

else:
    if n % 2 == 0:
        flag = False
    else:
        flag = True
        for i in range(2, int(n / 2)):
            if n % i == 0:
                flag = False
                break

    if flag:
        print("prime number")
    else:
        print("not prime number")
