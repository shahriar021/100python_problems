li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def map(x):return x%2==0

li2=list(filter(map,li))
print(li2)