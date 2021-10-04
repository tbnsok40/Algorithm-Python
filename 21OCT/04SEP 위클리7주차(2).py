from collections import deque, defaultdict


def solution(enter, leave):
    # for l in leave:
    #     if l not in room:
    #         while l not in room:
    #             room.append(enter.popleft())
    #     else:
    #         answer[l - 1] = len(room) - 1
    #         room.popleft()

    # while True:
    #     if leave[0] in room:
    #         answer[leave[0]] = len(room) - 1
    #         room.popleft()
    #         leave.popleft()
    #     else:
    #         room.append(enter.popleft())
    #         print(room)
    #
    #     if not room:
    #         break

    return
# enter = [1, 2, 3, 4]
# leave = [1, 4, 2, 3]
enter = [1, 3, 2]
leave = [1, 2, 3]
room = [1, 2, 3, 4]
# 1, 2, 3, 4 순으로 들어오는데, 2 에서 4 까지 같이 존재한다.
# 엔터를 룸에 우선 하나 넣고, 리브가 룸에 없으면, 엔터를 또 룸에 넣는다.
# 리브가 룸에 있을 때까지 엔터를 계속 룸에 넣는다.
# 리브가 룸에 있으면 len(room) - 1 로 저장. 그리고 룸에서 팝.

print(solution(enter, leave))
