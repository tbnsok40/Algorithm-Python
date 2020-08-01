li = [3,30,34,9]
li2 = []
one = []
dec = []
hund = []
thou = []
# for i in li:
#     if i < 10:
li.sort()
for idx, i in enumerate(li):
    if i > 10:
        li[:idx]

