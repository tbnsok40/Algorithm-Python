
board = [[11,13,15,16],[12,1,4,3],[10,2,7,8],[5,14,6,9]]
nums = [14,3,2,4,13,1,16,11,5,15]


from collections import defaultdict
def solution(board, nums):
    N = len(board)
    result = 0
    # hash_nums = defaultdict(int)
    # for num in nums:
    #     hash_nums[num] += 1
    # 이걸 set으로 그냥 바꾼다는 거지, 어차피 dict의 value는 1을 넘을수 없으니까
    # set의 시간복잡도는 O(1) => list에선 쓰지 못한 for i in list:를 쓸 수 있다.
    hash_nums = set(nums)

    right_count = 0
    left_count = 0
    for i in range(N):
        col_count = 0
        row_count = 0

        for j in range(N):
            if board[i][j] in hash_nums:
                col_count += 1
            if board[j][i] in hash_nums:
                row_count += 1

        if col_count == N:
            result += 1
        if row_count == N:
            result += 1

        if board[i][j] in hash_nums:
            left_count += 1
        if board[i][(len(board)-1) - i] in hash_nums:
            right_count += 1

    if left_count == N:
        result += 1
    if right_count == N:
        result += 1

    return result

print(solution(board,nums))

# 구해야 하는 것: 몇 빙고인지 숫자 값 => 어떤 줄이 빙고되는게 중요할까..?

# feed_back: set()은 리스트에 비해 순서를 따지지 않으므로, 시간복잡도가 대게 O(1)이 된다. (중요)

