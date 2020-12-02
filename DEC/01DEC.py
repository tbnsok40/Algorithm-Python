# 파이썬
import itertools

def get_next(cur_y, cur_x, cur_d):
    DELTAS = {'U': (-1, -1), 'D': (1, 0), 'R': (0, 1)}
    #print(DELTAS[1][0])
    print(cur_d)
    dy, dx = DELTAS[cur_d][0], DELTAS[cur_d][1]
    print(DELTAS[cur_d][0], DELTAS[cur_d][1])
    nxt_y, nxt_x = cur_y + dy, cur_x + dx
    return nxt_y, nxt_x


def check_turn(nxt_y, nxt_x, n, snail):
    return nxt_y < 0 or nxt_y >= n or nxt_x > nxt_y or snail[nxt_y][nxt_x] != 0


def solution(n):
    NEXT = {'U': 'D', 'D': 'R', 'R': 'U'}
    N = sum(range(1, n+1))
    snail = [[0] * i for i in range(1, n+1)]

    cur_y, cur_x, cur_d = 0, 0, 'D'
    for num in range(1, N+1):
        snail[cur_y][cur_x] = num
        if check_turn(*get_next(cur_y, cur_x, cur_d), n, snail):
            cur_d = NEXT[cur_d]
        cur_y, cur_x = get_next(cur_y, cur_x, cur_d)

    return list(itertools.chain(*snail))
print(solution(4))
# def solution(n):
#     # 부분 힙 n개 만들기
#     # 포문 돌면서 각 힙의 사이즈에 맞게 넣기 => heapq[0]이 곧 length
#     # direction: down, left, up
#     # 배열을 down, left, up(은 스택으로 쌓아야할듯)으로 나눠서 값 저장?
#     up = deque()
#     sum = (1 + n) * n / 2
#     # 1부터 sum까지 수를 계속 뿌려주긴 해야한다.
#     # 그러면서 n만큼 채우면, n을 차감시켜서 다른 배열에 저장시키고
#
#     return n