# class CircularQueue:
#
#     def __init__(self, n):
#         self.maxCount = n
#         self.data = [None] * n
#         self.count = 0
#         self.front = -1
#         self.rear = -1
#
#
#     def size(self):
#         return self.count
#
#     def isEmpty(self):
#         return self.count == 0
#
#     def isFull(self):
#         return self.count == self.maxCount
#
#     def enqueue(self, x):
#         if self.isFull():
#             raise IndexError('Queue full')
#         self.rear = (self.rear + 1) % self.maxCount
#
#         self.data[self.rear] = x
#         self.count += 1
#
#     def dequeue(self):
#         if self.isEmpty():
#             raise IndexError('Queue empty')
#         self.front = (self.front + 1) % self.maxCount
#
#         x = self.data[self.front]
#
#         self.count -= 1
#         return x
#
#     def peek(self):
#         if self.isEmpty():
#             raise IndexError('Queue empty')
#         return self.data[(self.front+1)%self.maxCount]
#     def display(self):
#         print(self.data)
#
# if __name__ =='__main__':
#     cq = CircularQueue(number)
#     for i in range(1, number+1):
#         cq.enqueue(i)
#     # (cq.enqueue(1))
#     # (cq.enqueue(2))
#     # (cq.enqueue(3))
#
# print(cq.data)
## 환형 큐 사용 시도. 좋은 시도였다.


# 요세푸스
import sys
def read(): return map(int, sys.stdin.readline().split())
number,skip,start = read()
stones = list(range(1,number+1))

idx = start-1
skip = skip -1
del stones[idx]
# 문제는 시작점이 있다는 것.
while len(stones) >1:
    idx += skip
    if len(stones) < idx + skip:
        idx = (idx+skip) % len(stones)
    print(stones)
    del stones[idx]
    print(stones)
print(stones)
