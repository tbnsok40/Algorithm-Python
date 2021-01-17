from itertools import permutations
import re
expression = "100-200*300-500+20"
# 정규 표현식을 이용한 풀이
def solution(expression):
    # expressions = set(re.findall("\D", expression)) # 정규식 편하네
    prior = permutations(set(re.findall("\D", expression)))
    cand = []
    for op_cand in prior:
        temp = re.split(r'(\D)',expression) # ['100', '-', '200', '*', '300', '-', '500', '+', '20']
        for exp in op_cand:
            while exp in temp:
                idx = temp.index(exp)
                temp = temp[:idx-1] + [str(eval(''.join(temp[idx-1:idx+2])))] + temp[idx+2:]
                # 정규식 사용으로 훨씬 간편하게 풀이의 군더더기를 줄였다.

        cand.append(abs(int(temp[0])))
    return max(cand)
# https://velog.io/@tjdud0123/%EC%88%98%EC%8B%9D-%EC%B5%9C%EB%8C%80%ED%99%94-2020-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9D%B8%ED%84%B4%EC%8B%AD-%EB%AC%B8%EC%A0%9C
print(solution(expression))

# 재귀를 이용한 풀이
# def calc(priority, n, expression):
#     if n == 2:
#         return str(eval(expression))
#     if priority[n] == '*':
#         res = eval('*'.join([calc(priority, n + 1, e) for e in expression.split('*')]))
#     if priority[n] == '+':
#         res = eval('+'.join([calc(priority, n + 1, e) for e in expression.split('+')]))
#     if priority[n] == '-':
#         res = eval('-'.join([calc(priority, n + 1, e) for e in expression.split('-')]))
#     return str(res)
#
# def solution(expression):
#     answer = 0
#     priorities = [
#         ('*', '-', '+'),
#         ('*', '+', '-'),
#         ('+', '*', '-'),
#         ('+', '-', '*'),
#         ('-', '*', '+'),
#         ('-', '+', '*')
#     ]
#     for priority in priorities:
#         res = int(calc(priority, 0, expression))
#         answer = max(answer, abs(res))
#
#     return answer
#https://medium.com/@haeseok/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%98%EC%8B%9D-%EC%B5%9C%EB%8C%80%ED%99%94-eaa534d55316


# mine
# def solution(s):
#     re_count = ['*', '+', '-']
#     count = []
#     for i in s:
#         if i in re_count and i not in count:
#             count.append(i)
#
#     origin = []
#     small = ''
#     for i in s:
#         if i not in count:
#             small += i
#         else:
#             origin.append(small)
#             small = ''
#             origin.append(i)
#     origin.append(small)
#
#     ans = []
#     for i in permutations(count, len(count)):
#         temp = origin[:]
#         result = count_permu(temp, i)
#         ans.append(result)
#
#     return max(ans)
#
#
# def count_permu(temp, permus):
#     # print(permus)
#     for i in permus:
#         for idx, j in enumerate(temp):
#             if j == i:
#                 # print(temp)
#                 re = (eval(''.join(temp[idx - 1: idx + 2])))
#                 # print(re)
#                 temp[idx] = str(re) # str() 처리를 안해주면 join에서 int로 인식되기에 오류
#                 # print('1',temp)
#                 del temp[idx + 1]
#                 del temp[idx - 1]
#
#                 # temp.remove(temp[idx + 1])
#                 # temp.remove(temp[idx - 1])
#                 # print(temp)
#
#
#     # print('temp: ', temp, permus, i)
#     if len(temp) > 1:
#         return abs(eval(''.join(temp)))
#     else:
#         return abs(int(temp[0]))