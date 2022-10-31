l = [0] * 101
l[1] = 1
l[2] = 1
l[3] = 1

answer = []
for _ in range(int(input())):
    answer.append(int(input()))

for i in range(4, max(answer) + 1):
    l[i] = l[i - 3] + l[i -2]

for i in answer:
    print(l[i])