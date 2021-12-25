s=input()
d={"upper":0,"lower":0}
for i in s:
    if i.isupper():
        d["upper"]+=1
    elif i.islower():
        d["lower"]+=1
print("upper",d["upper"],"lower",d["lower"])            