# 백만
from collections import deque
def solution(phone_book):
    sorted_book = deque(sorted(phone_book))
    # 이제 앞뒤로만 비교하면 된다.
    
    while sorted_book:
        try:
            alpha, beta = sorted_book.popleft(), sorted_book.popleft()
            if beta.startswith(alpha):
               return False
        except:
            return True

phone_book = ['119', '97674223', '1195524421']
phone_book = ['123','456','789']
print(solution(phone_book))