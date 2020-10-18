import sys
read = list(map(int, sys.stdin.readline().split()))
#mapping 시키는 거니까 당연히 변수 두개를 끌고와야지 ㅡㅡ

songs = read[0]
average = read[1]-1
semi = songs * average
print(semi+1)


# 고수의 답
a,i = map(int,input().split())
print(a*(i-1))
