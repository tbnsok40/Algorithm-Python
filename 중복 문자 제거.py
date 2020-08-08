# a = input()
# list2 = list(a)
# print(list2)
# dictionary = {}
# for i in list2:
#     try:
#         dictionary[i] = 1
#
#     except:
#         dictionary[i] = 1
# print(''.join(sorted(list(dictionary.keys()))))
s = 'cbacdcbc'
s[2] = 'c'
print(s)
print(sorted(set(s)))
print(s[s.index('a'):])
def remove(self, s:str)->str:
    for char in sorted(set(s)):
        suffix = s[s.index(char)]