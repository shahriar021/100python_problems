
def feb(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return feb(n-1)+feb(n-2)


n = int(input())
v=[str(feb(x)) for x in range (0,n+1)]
print(",".join(v))
