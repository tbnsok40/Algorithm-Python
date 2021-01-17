# 시간 복잡도 n^2 => bad
def solution(n, arr1, arr2):
    arr1_, arr2_,big = [],[],[]
    for a, b in zip(arr1, arr2):
        small = ''
        # 여기를 굳이 for문으로 분해할 필요가 없었다.
        for i in bin(a | b)[2:]:
            small += i
        while len(small) != n:
            small = '0' + small
        # replace 연속 사용 가능
        big.append(small.replace('0',' ').replace('1','#'))
    return big

# rjust 개꿀
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a12 = (bin(i|j)[2:])
        a12 = a12.rjust(n,'0').replace('1','#').replace('0',' ')
        answer.append(a12)
    return answer

