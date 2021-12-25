lis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(x): return x % 2 == 0


lis2 = list(filter(is_even, lis1))


print(lis2)
