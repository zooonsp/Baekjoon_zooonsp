n, m = map(int, input().split())
S = []
strings = []
for _ in range(n):
    S.append(input())

for _ in range(m):
    strings.append(input())

answer = 0
for i in strings:
    if i in S:
        answer += 1
        
print(answer)