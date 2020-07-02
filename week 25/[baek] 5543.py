li = []
for _ in range(5):
    li.append(int(input()))
print(min(li[:3]) + min(li[3:]) - 50)