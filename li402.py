v=input()
n=[x for x in v.split(",") if int(x)%2!=0]
print(",".join(n))