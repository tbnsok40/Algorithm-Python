
inputs = input()
print('inputs:',(inputs))
inputs =inputs.strip('R') # 중간letter는 왜 strip안돼?
print(inputs)
inputs = inputs.replace('C',',')
inputs = list(inputs.split(','))
print(inputs)

# print(inputs.strip('C'))
# print(chr(col + 64))
# # col_answer = (col//27) + (col % 27)
# # num = int2str(col)
# # print(num)
# print(chr(65))

