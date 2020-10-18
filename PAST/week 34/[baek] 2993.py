# strings = list(input())
# print(strings) # list는 모두 한letter단위로 반환한다.
# import sys
# def read(): return sys.stdin.readline().rstrip()
#readline을 쓰면 개행을 같이 읽어들인다.
before = input()
final = before
for i in range(len(before)-2):

    for j in range(i+2, len(before)):
        fir = before[:i+1][::-1]
        sec = before[i+1:j][::-1]
        thr = before[j:][::-1]
        full = fir + sec + thr
        # print('full: ',full, 'before:',before)

        # if full < before:
        #     final = full
        if full < final:
            final = full
print(final)