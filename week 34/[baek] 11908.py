# import sys
# def read(): return map(int, sys.stdin.readline().split())
#
# N = int(sys.stdin.readline())
# num_list = list(read())
# print(sum(num_list[:-1]))
import sys
N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
print(sum(num_list[:-1]))
