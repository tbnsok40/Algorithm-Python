# def solution(s):
#     hash_p = [hash('p'), hash('P')]
#     hash_y = [hash('y'), hash('Y')]
#     count_p, count_y = 0, 0
#     for letter in s:
#         if hash(letter) in hash_p:
#             count_p += 1
#         elif hash(letter) in hash_y:
#             count_y += 1
#     if count_p == count_y:
#         return True
#     else:
#         return False

def solution(s):
    return s.lower().count('p') == s.lower().count('y')