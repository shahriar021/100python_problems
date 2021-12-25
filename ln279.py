v = []
items = [x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp % 5:
        v.append(p)

print (','.join(v))


p=input()
c=int(p,2)
print(c)
