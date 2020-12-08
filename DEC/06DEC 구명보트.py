
# from itertools import product
# def solution(numbers, target):
#
#     return
people = [70,80,50]
limit = 100

people = [15, 20, 30, 40, 45, 50, 60,85,90]
limit = 100
from collections import deque
from itertools import islice

def solution(people, limit):
    #1 오름차순 정렬
    #2 리턴값을 최대한 작게
    #3 작은 배열에 담는다 리미트 안 때릴때가지

    # 발상 전환: 오름차순 대신 내림차순으로 가보자.
    count = 0

    sorted_people = sorted(people)
    sorted_people = deque(sorted_people)

    while sorted_people:
        count += 1
        temp_people = islice(sorted_people,0, len(sorted_people)-1)
        # temp_people = sorted_people[:-1]

        store = 0
        for i in temp_people:
            if i + sorted_people[-1] <= limit:
                store = i
            else:
                # count += 1
                break

        if store != 0:
            sorted_people.remove(store)
        # sorted_people.remove(sorted_people[-1])
        sorted_people.pop()

    return count

# 강제로 deque형 변환 했음에도 효율성을 뚫지 못하기에
# 풀이 구조 자체를 바꿔야 한다.

print(solution(people, limit))
