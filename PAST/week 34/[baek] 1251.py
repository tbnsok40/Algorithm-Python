import sys
def read(): return sys.stdin.readline().rstrip()
before = read()
final = before[::-1]
for i in range(len(before)-2):
    for j in range(i+2, len(before)):
        fir = before[:i+1][::-1]
        sec = before[i+1:j][::-1]
        thr = before[j:][::-1]
        full = fir + sec + thr

        if (full < final):
            final = full
            # 반례 abcd => abdc로 출력돼야하는데, 초기값 포함때문에 abcd로 출력돼
print(final)

# if final < before:
#     print(final)
# else:
#     print(before)