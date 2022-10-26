l = [0 for _ in range(31)]
for _ in range(28):
    x = int(input())
    l[x] += 1

for i in range(1, 31):
    if l[i] == 0:
        print(i)
