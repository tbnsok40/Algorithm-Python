numbers = [int(input()) for _ in range(5)]

multiplied = 1
for number in numbers:
    multiplied *= number
    if multiplied**(0.5) == int(multiplied**0.5):
        print('found')
        break
else:
    print('not found')