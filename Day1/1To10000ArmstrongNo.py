for no in range(1, 10000):

    temp = no
    sum = 0
    count = len(str(no))

    while temp > 0:
        rem = temp % 10
        sum = sum + (rem ** count)
        temp = temp // 10

    if no == sum:
        print(no)