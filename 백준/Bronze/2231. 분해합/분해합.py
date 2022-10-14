n = int(input())
xn = n
answer = 0
che = []
while xn > 1:
    xn -= 1
    l = list(map(int, str(xn)))
    answer = xn + sum(l)
    if answer == n:
        che.append(xn)

if len(che) > 0:
    print(che[-1])
else:
    print(0)