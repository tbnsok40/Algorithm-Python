N = int(input())  # 1 ~ 12


def factorial(N):
    if N <= 1:
        return 1

    return N * factorial(N - 1)


print(factorial(N))


"""
0 ~ 12
"""
