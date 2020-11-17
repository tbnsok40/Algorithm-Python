S = "3 DUP 5 - -"
S = "13 DUP 4 POP 5 DUP + DUP + -"
S = "5 6 + -"

def solution(S):
    S = S.split(' ')
    temp = []
    for i in S:
        try:
            if i == 'DUP':
                temp.append(temp[-1])

            elif i == 'POP':
                temp.pop()

            elif i == "+":
                alpha = temp.pop()
                beta = temp.pop()
                temp.append(int(alpha)+int(beta))

            elif i == '-':
                alpha = temp.pop()
                beta = temp.pop()
                if int(alpha)-int(beta) < 0:
                    return -1
                temp.append(int(alpha)-int(beta))
            else:
                temp.append(i)

        except IndexError or OverflowError:
            return -1
    return temp[-1]
print(solution(S))

