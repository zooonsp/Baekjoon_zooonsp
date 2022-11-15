n = int(input())

s = [0 for _ in range(301)]
che = [0 for _ in range(301)]

for i in range(n):
    s[i] = int(input())

che[0] = s[0]
che[1] = s[0] + s[1]
che[2] = max(s[0] + s[2], s[1] + s[2])

for i in range(3, n):
    che[i] = max(che[i - 3] + s[i-1] + s[i], che[i - 2] + s[i])

print(che[n-1])