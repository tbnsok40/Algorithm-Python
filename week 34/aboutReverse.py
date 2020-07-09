#string을 reverse하는 방법
a = 'abcde'
print(a[3::-1])

b = 'fghijk'
print(b[5::-1])
print(b[::-1]) #5가 마지막 인덱스이므로 생략 가능

c = 'happiness'
print(('').join(reversed(c)))

# list를 reverse
d = '1234'
s = list(d)
s.reverse()
print(''.join(s))