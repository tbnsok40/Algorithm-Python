number = 10


def dectobi(num):
    bi = ''
    while True:
        a, b = divmod(num, 2)
        num = a
        bi += str(b)
        if a == 1:
            bi += str(a)
            return bi[::-1]


print(dectobi(number))
