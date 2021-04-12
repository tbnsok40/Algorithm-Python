import heapq


def solution(jobs):
    start, answer, now, i = -1, 0, 0, 0
    heap = []
    # O(n^2)
    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])

        while heap:
            # curr[0]: 소요시간, curr[1]: 출발 시
            curr = heapq.heappop(heap)
            start = now
            now += curr[0]
            answer += (now - curr[1])
            i += 1
        else:
            # 현재 처리가능한 작업이 없다면,
            # 남아있는 작업의 요청 시간이 아직 오지 않은 것이기에,
            # 현재 시점(now)을 +1 해준다.
            now += 1
    return int(answer / len(jobs))
# 간단한 코든데 미친 로직이네


jobs_ = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs_))


def solution2(jobs):

    # start를 -1로 해야, 시작 시점 0초를 커버할 수 있다.
    start, answer, now, i = -1, 0, 0, 0
    heap = []
    while i < len(jobs):
        # 1차 반복문
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
                # 처리하는데 걸리는 (짧은) 시간 기준으로 heap 에 넣는다.
                # 단, 시작 시간이 가장 먼저인 것으로.

        # 2차 반복
        while heap:
            curr = heapq.heappop(heap)

            start = now
            now += curr[0]
            answer += (now - curr[1])
            i += 1
        else:
            now += 1
    return int(answer / len(jobs))

