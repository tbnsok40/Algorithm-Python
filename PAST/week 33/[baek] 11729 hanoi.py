


#1 from, to, aux : 1, 3, 2
# def hanoi(n, fromm, to, aux):
#     if n==1:
#         print(fromm, to)
#         return
#     hanoi(n-1, fromm, aux, to)
#     print(fromm, to)
#     hanoi(n-1, aux, to, fromm)

#2 begin, aux, end : 1, 2, 3
n = int(input())
block = list()
def hanoi(n, begin, aux, end):
    if n == 1:
        block.append([begin, end])
    else:
        hanoi(n-1, begin, end, aux)
        hanoi(1, begin, aux, end)
        hanoi(n-1, aux, begin, end)

hanoi(n,1,2,3)

print(len(block))
for i in block:
    print(*i)
