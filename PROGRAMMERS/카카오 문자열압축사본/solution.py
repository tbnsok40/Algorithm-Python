s = "ababcdcdababcdcd"
def solution(s):
    answer = len(s)
    for size in range(1, len(s) // 2 + 1):
        count = 1
        compress = 0
        prev = s[:size] # size가 2라면 초기 두 문자를 prev에 할당
        for i in range(size, len(s) + size, size): # range()세번째 메서드 활용, '증감 범위'
            curr = s[i: i + size] # i도 결국 size가 돼. size 크기만큼 증가하니까
            # 즉 curr은 size 범위만큼 할당하게 되는 문자열
            if prev == curr:
                count += 1
            else:
                print('i:',i, 'compress:',compress,'size:',size, 'len(str(count)):',len(str(count)), 'count:',count, 'len(prev):',prev)

                compress += size + len(str(count)) if 1 < count else len(prev)
                # count가 1보다 크다: 앞뒤가 한번씩은 같은적이 있다. 즉 숫자 n이 문자 앞에 붙을 것인데
                # 이는 숫자 n이 얼마나 크던 간에 길이는 1밖에 되질 않는다.(물론 두자릿수 되면 2니까 len()을 써줬네)

                prev = curr
                count = 1
        answer = min(answer, compress) #바깥 for문에 의해 size 크기 만큼 업데이트 된다.
    return answer
print(solution(s))


# com = 2
# count = 3
# prev = 'abc'
# com += com + len(str(count)) if 1 < count else len(prev)
# print(len(str(count)))
# print(com)