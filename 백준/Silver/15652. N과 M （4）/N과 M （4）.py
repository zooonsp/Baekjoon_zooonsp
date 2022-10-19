from itertools import combinations_with_replacement

n, m = map(int, input().split())
l = [str(i) for i in range(1, n + 1)]

answer = list(combinations_with_replacement(l, m))


for i in answer:
    print(" ".join(i))