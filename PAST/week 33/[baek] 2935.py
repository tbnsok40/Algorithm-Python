import sys
def read(): return sys.stdin.readline()

word1 = int(read())
word2 = (read().split('\n'))
word3 = int(read())

if word2[0] == '*':
    print(word1*word3)
else:
    print(word1 + word3)
