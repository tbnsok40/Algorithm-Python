a = [1,2,3,4,5,6,7,8,9,0]
b = [11,4,5,2,9,0,1,-1,1,1]
trans = lambda a,b: sum((1 if x+y > 10 else 0) for x, y in zip(a,b))
sett = set(filter(lambda a: trans(a,b),a))
print(sett)