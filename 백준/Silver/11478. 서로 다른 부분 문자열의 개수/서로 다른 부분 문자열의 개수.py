l = list(input())
answer = []
for i in range(1, len(l) + 1):
    s = 0
    f = i
    while f != len(l) +1:
        answer.append("".join(l[s:f]))
        s += 1
        f += 1
answer = set(answer)
print(len(answer))