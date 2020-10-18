# tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
# tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
tickets = [['ICN','B'],['ICN','C'],['D','ICN'],['C','D']]
from collections import deque as queue
def solution(tickets):
    # dictionary 정렬/정리
    d,q,answer = dict(), queue(), list()
    for from_, to_ in  tickets:
        try:
            d[from_] += [to_]
        except:
            d[from_] = [to_]
    for key_ in d.keys():
        d[key_].sort(reverse=True)
    print('dict:',d)
    ######################################
    stack = ['ICN']
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in d or len(d[top]) == 0:
            path.append(stack.pop())
            print(path)
        else:
            # print('answer',stack)
            stack.append(d[top].pop())
    return path[::-1]
print(solution(tickets))


