def solution(n):
    binary = bin(n)[2:].count('1')
    while True:
        n += 1
        if binary == bin(n)[2:].count('1'):
            return n