
# from itertools import product
# def solution(numbers, target):
#
#     return
people = [70,80,50]
limit = 100

people = [15, 20, 30, 40, 45, 50, 60,85,90]
limit = 100

def solution(people, limit):
    count = 0
    sorted_people = sorted(people)

    while sorted_people:
        count += 1
        last = sorted_people.pop()
        temp_people = sorted_people
        store = 0
        for i in temp_people:
            if i + last <= limit:
                store = i
            else:
                break
        if store != 0:
            sorted_people.remove(store)
        print(sorted_people)

    return count


def solution(people, limit):
    count = 0
    sorted_people = sorted(people)

    start = 0
    end = len(sorted_people) - 1


    while start <= end:
        count += 1
        if sorted_people[start] + sorted_people[end] <= limit:
            start += 1
            end -= 1 # 애초에 두명'만' 태울 수 있음에 의하면 end를 빼주는게 맞지.
        else:
            end -= 1

    return count

# 강제로 deque형 변환 했음에도 효율성을 뚫지 못하기에
# 풀이 구조 자체를 바꿔야 한다.
# islice()를 배웠네
print(solution(people, limit))
# 깊은 고민은 깊은 실력을 만든다.
