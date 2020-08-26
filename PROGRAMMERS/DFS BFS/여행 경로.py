# tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
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
        d[key_].sort()
    ###################
    answer.append('ICN')
    curr = answer[-1]

    while len(answer) < len(tickets)+1:
        curr = d[curr].pop(0)
        answer.append(curr)
        curr = answer[-1]
        # print(d)
    return answer
print(solution(tickets))

# genres_in_order = sorted(songs_in_genres.keys(), key=lambda x: songs_in_genres[x], reverse=True)