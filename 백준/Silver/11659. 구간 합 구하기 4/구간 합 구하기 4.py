import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
sumList = [0]

s = 0
for i in l:
    s += i
    sumList.append(s)

for i in range(m):
    x, y = map(int, input().split())
    print(sumList[y] - sumList[x-1])