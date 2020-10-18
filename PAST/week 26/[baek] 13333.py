# ICPC 대학은 q-인덱스라는 값을 정의했다. 이 인덱스는 논문들의 중요도를 측정하기 위해,
# 가장 많이 인용된 논문들의 개수와 그 논문들의 인용횟수를 이용하여 다음과 같이 정의된다.
# 한 학생이 발표한 총 n ≥ 1 편의 논문 중에서, k번 이상 인용된 논문이 k편 이상이고
# 나머지 n − k 편의 논문들 인용회수가 각각 k 번 이하라면, 해당 학생의 q-인덱스는 k이다.
#
# 예를 들어, 한 학생이 발표한 논문이 총 5 편이고, 각 논문의 인용횟수가 8, 4, 5, 3, 10 이라 하자.
# 한 번 이상 인용된 논문이 1 편 이상이지만 나머지 4 편의 논문 중에는
# 한 번 보다 더 많이 인용된 논문이 존재하기 때문에 q-인덱스는 1 이 아니다.
# 그리고 모든 논문이 5 번 이상 인용되지 않았기 때문에, 인덱스 값이 5 가 될 수도 없다.
# 이 학생의 q-인덱스는 결국 4 가 되는 데, 그 이유는 4 번 이상 인용된 논문 4 편이 있고, 나머지 1 편은 4 번 이하의 인용횟수를 갖기 때문이다.

# n번의 논문 제출: len(n)
n = int(input())
papers =list(map(int, input().split()))
# for _ in range(n):
#     papers.append(int(input()))
# [8, 4, 5, 3, 10]
# [3,4,5,8,10]
papers = sorted(papers)
# step1) k번 이상 인용된 논물이 k편 이상: n[i] > n[j] ==> count ++ ==> count <= k
count = 0
qindex = 0

for i in range(n):
    count = 1
    for j in (papers[i+1:]):
        if papers[i] < j:
            count += 1
            print('count: ',count)
            # if count == papers[i]:
            #     break
    if count >= papers[i]: #step1 충족
        print('i: ',i)
        if papers[i] <= len(papers[i:]):  # step1 satisfied
            print(papers[i], papers[i:])
            count = 0
            for j in (papers[:i]):
                print('j:', j)

                print('papers[:%d],' % i, papers[:i])

                if j <= papers[i]:
                    count += 1
                    if count == len(papers[:i]):
                        qindex = papers[i]
                        print('qindex:', qindex)


    else:
        continue

# step2) 나머지 n-k(>=0)편의 논문들 인용횟수가 k이하이면 인덱스는 k.
# for i in range(n):
#     print(i)
#     if papers[i] <= len(papers[i:]): #step1 satisfied
#         print(papers[i], papers[i:])
#         for j in (papers[:i]):
#             print('j:',j)
#
#             print('papers[:%d],'%i ,papers[:i])
#             if j <= papers[i]:
#                 qindex = papers[i]
#                 print('qindex:',qindex)
print(qindex)
print(papers)
