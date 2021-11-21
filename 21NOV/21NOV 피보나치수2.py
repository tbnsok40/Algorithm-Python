def fibo(m):
    global count_zero
    global count_one
    if m == 0:
        count_zero += 1
        return 0
    if m == 1:
        count_one += 1
        return 1
    if res[m] != 0:
        return res[m]
    else:
        return fibo(m - 1) + fibo(m - 2)


def __main__():
    N = int(input())
    global res
    global count_zero
    global count_one

    res = [0] * (N + 1)
    res[1] = 1

    for _ in range(N):

        count_zero = 0
        count_one = 0


        M = int(input())
        fibo(M)
        print(count_zero, count_one)
    return


__main__()

"""
3
0
1
3
"""
