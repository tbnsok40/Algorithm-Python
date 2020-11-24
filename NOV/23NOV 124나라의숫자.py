def solution(n):

    a, b = divmod(n, 3)
    if b == 0:
        last = "4"
    elif b == 2:
        last = "2"
    else:
        last = "1"



    answer = ''
    return answer