
def feb(n):
    if n==1:
        return 1
    elif n==0:
        return 0    
    else:return feb(n-1)+feb(n-2)


n = int(input())
print(feb(n))    
