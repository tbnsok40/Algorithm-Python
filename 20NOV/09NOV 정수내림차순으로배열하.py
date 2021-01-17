def solution(n):
    # arr = sorted(list(str(n)), reverse = True)
    # 꼭 list로 감쌀 필요가 없다. str은 sorted()하면 알아서 list로 쪼개진다.
    arr = sorted(str(n), reverse = True)
    return int(''.join(arr))
n = 8421523
print(solution(n))