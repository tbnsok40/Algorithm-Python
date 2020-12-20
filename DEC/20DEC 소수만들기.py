from itertools import combinations
def solution(nums):
    N = len(nums)
    count = 0
    for i in combinations(nums, 3):
        if sosu(sum(i)):
            count += 1

    return count


def sosu(nums):
    for i in range(2, nums):
        if nums % i == 0:
            return False
    return True


nums = [1, 2, 7, 6, 4]
print(solution(nums))
