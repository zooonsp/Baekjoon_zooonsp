import sys

input = sys.stdin.readline
N, M = map(int, input().split())
l = list(map(int, input().split()))

s = [0] * N
c = [0] * M
answer = 0

s[0] = l[0]
for i in range(1, N):
    s[i] = s[i - 1] + l[i]

for i in range(N):
    div = s[i] % M
    if div == 0:
        answer += 1
    c[div] += 1

for i in range(M):
    if c[i] > 1 :
        answer += (c[i] * (c[i] - 1) // 2)

print(answer)