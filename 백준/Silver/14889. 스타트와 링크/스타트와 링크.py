from itertools import combinations

n = int(input())
s = []
for _ in range(n):
    s.append(list(map(int, input().split())))
    
team = []
for i in combinations(list(range(n)), n // 2):
    team.append(i)
# -1 ~ -(len(tema) // 2): 상대팀
minv = 987654321
for t in range(len(team) // 2):
    st = team[t]
    lt = team[-t -1]
    ss = 0
    ls = 0
    for i in combinations(st, 2):
        ss += (s[i[0]][i[1]] + s[i[1]][i[0]])
    for i in combinations(lt, 2):
        ls += (s[i[0]][i[1]] + s[i[1]][i[0]])

    if minv > abs(ss - ls):
        minv = abs(ss - ls)
print(minv)