# 백만
from collections import deque
def solution(phone_book):
    sorted_book = deque(sorted(phone_book))
    # 이제 앞뒤로만 비교하면 된다.
    # 앞에 길이만큼 뒤에 문자 슬라이싱 해서 비교하는 방법도 존재
    while sorted_book:
        try:
            alpha = sorted_book.popleft()
            if sorted_book[0].startswith(alpha):
               return False
        except:
            return True

    # except문에서 끝내면 안돼고, 밑에 return True도 써줘야한다.
    return True

phone_book = ['119', '97674223', '1195524421']
phone_book = ['123','456','789']
phone_book = ['123']
print(solution(phone_book))