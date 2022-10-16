n = int(input())
nl = list(map(int, input().split()))

cd = {}

for i in nl:
    if i in cd:
        cd[i] += 1
    else:
        cd[i] = 1

m = int(input())
ml = list(map(int, input().split()))

answer = []
for i in ml:
    if i in cd:
        answer.append(str(cd[i]))
    else:
        answer.append("0")
print(" ".join(answer))