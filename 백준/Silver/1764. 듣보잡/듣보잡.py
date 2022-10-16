n, m = map(int, input().split())

l1 = set([input() for _ in range(n)])
l2 = set([input() for _ in range(m)])

answer = l1 & l2
answer = sorted(answer)
print(len(answer))
for i in answer:
    print(i)