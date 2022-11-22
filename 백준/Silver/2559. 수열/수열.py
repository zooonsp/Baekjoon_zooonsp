n, k = map(int, input().split())
l = list(map(int, input().split()))

s = sum(l[:k])
r = s
for i in range(k, n):
    s += l[i] - l[i-k]
    r = max(r, s)

print(r)