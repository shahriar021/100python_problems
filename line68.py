d=dict()
def intgrl(x):
    for i in range(1,x+1):
        d[i]=i*i
    return d
x=int(input())
print(intgrl(x))