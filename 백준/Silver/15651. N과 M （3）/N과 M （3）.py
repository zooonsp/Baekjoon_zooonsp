from itertools import product

n, m = map(int, input().split())
l = [str(i) for i in range(1, n + 1)]

answer = list(product(l, repeat = m))

for i in answer:
    print(" ".join(i))