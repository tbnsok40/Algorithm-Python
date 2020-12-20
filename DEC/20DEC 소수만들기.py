from itertools import combinations
def solution(nums):
    return sum([1 for i in combinations(nums, 3) if sosu(sum(i))])


def sosu(nums):
    for i in range(2, nums):
        if nums % i == 0:
            return False
    return True