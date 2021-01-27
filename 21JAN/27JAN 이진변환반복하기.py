s = '111011001'
count =0
# 0을 제거하는 횟수 저장해야하고, count += 1
# 이진숫자로 변경되는 횟수 저장해야한다. bin() 메소드 사용횟수
# while a != 1:
def solution(s):
    c = 0
    count = 0
    while s != '1':
        c += s.count('0')
        s = s.replace('0','')
        s = str(bin(len(s))[2:])
        count += 1
    return [count, c]
print(solution(s))
# 0 제거 후 1의 길이 => X
# binary(X)


a = 6
print(bin(a)[2:])
print()