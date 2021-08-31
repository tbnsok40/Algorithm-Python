# 2^n 중 n 이 무엇이지
# n 을 -1 씩 해가면서 탐색한다. 2^n // 2
# n = 2 ,  0, 1 || 2, 3
# n = 3 ,  0, 1, 2, 3 || 4, 5, 6, 7
# n = 4,   0, 1, 2, 3, 4, 5, 6, 7, || 8, 9, 10, 11, 12, 13, 14, 15


# n 일 때, 처음 이등분한 길이는 0 ~ 2 ^ (n - 1) - 1 이다.
# 뒤의 이등분 길이는 2 ^ (n - 1) ~ (2 ^ n) - 1

from math import sqrt, pow


#
# def solution(arr):
#     N = len(arr)
#     n = len(bin(N)[2:]) - 1
#
#     dx = [1, -1, 0, 0]
#     dy = [0, 0, 1, -1]
#
#     init = [0, 0]
#
#     while n > 1:
#
#         first = [i for i in range(2 ** (n - 1))]
#         second = [i for i in range(2 ** (n - 1), 2 ** n)]
#         # print(first, second)
#         count1 = 0
#         same = True
#         for r in first:
#             for c in first:
#                 if arr[r][c] != arr[first[0]][first[0]]:
#                     same = False
#                     break
#             if same == False:
#                 break
#         else:
#             print(same)
#
#     return answer
#
def solution(arr):
    N = len(arr)
    answer = [0, 0]

    def compress(x, y, N):
        init = arr[x][y]
        for r in range(x, x + N):
            for c in range(y, y + N):
                if arr[r][c] != init:
                    N //= 2
                    compress(x, y, N)
                    compress(x, y + N, N)
                    compress(x + N, y, N)
                    compress(x + N, y + N, N)
                    # 리턴은 여기있어야한다. why?

        answer[init] += 1
        # return   리턴이 여기있으면 틀린다.
    compress(0, 0, N)
    return answer


arr = [[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]
print(solution(arr))

# 접근 방향의 차이 => 나는 무조건 사분면으로 나눠서 시도하려했는데 오히려 헷갈리기만 햇다.
# 이 풀이는 전체 매트릭스를 기준으로 우선 시작한다.
# 그리고 사분면을 쪼개면서 작두 타듯이 재귀를 탄다.


