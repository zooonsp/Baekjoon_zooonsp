n = int(input())
l = []
l.append([int(input())])
for _ in range(1, n):
    l.append(list(map(int, input().split())))

for i in range(1, n):
    if i == 1:
        l[1][0] += l[0][0]
        l[1][1] += l[0][0]
    else:
        for j in range(i + 1):
            if j == 0:
                l[i][0] += l[i-1][0]
            elif j == i:
                l[i][j] += l[i-1][j-1]
            else: # 첫번째와 마지막번째 사이
                l[i][j] += max(l[i-1][j-1], l[i-1][j])

print(max(l[n-1]))