def solution(tickets):
    result = ['ICN']
    while tickets:
        tmp = []
        # 담고 재정렬
        for idx in range(len(tickets) - 1, -1, -1):
            if result[-1] == tickets[idx][0]:
                tmp.append(tickets.pop(idx))  # tickets.pop(idx) == tickets[idx]
        if tmp:
            tmp.sort(reverse=True)
            result.append(tmp.pop()[1])
            tickets += tmp
        # print(tickets)
    return result


ticket = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

print(solution(ticket))
# 모든 순서를 방문할 수 있다.
# 같은 경로 존재시, 알파벳순으로 방문
# 함정: 무조건 첫번째 인덱스가 시작포인트 아니다. 이것도 sort로 검사해야함
