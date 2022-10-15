pl = [0 for _ in range(10000001)]
ml = [0 for _ in range(10000000)]
answer = []
n1 = input()
fl = list(map(int, input().split()))
for i in fl:
    if i < 0:
        ml[i] = 1
    else:
        pl[i] = 1
n2 = input()
sl = list(map(int, input().split()))
for i in sl:
    if i < 0:
        if ml[i] == 1:
            answer.append(str(1))
        else:
            answer.append(str(0))
    else:
        if pl[i] == 1:
            answer.append(str(1))
        else:
            answer.append(str(0))
answer = " ".join(answer)
print(answer)