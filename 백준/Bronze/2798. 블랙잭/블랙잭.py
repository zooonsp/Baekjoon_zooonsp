from itertools import combinations

n, m = map(int, input().split())
l = list(map(int, input().split()))

answer = 0

for i in combinations(l, 3):
    s = sum(i)
    if s >= answer and m >= s:
        answer = s
print(answer)
