# def solution(phone_book):
#     phone_book.sort()
#     answer = True
#     for i,j in zip(phone_book, phone_book[1:]):
#         if j.startswith(i):
#             answer =  False
#         else:
#             pass
#     return answer

phone_book = ['123','1234','67']

# 해시를 이용한 풀이
def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:

                answer = False
    return answer
print(solution(phone_book))