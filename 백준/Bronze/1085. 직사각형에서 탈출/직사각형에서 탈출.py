x, y, w, h = map(int, input().split())

answer = []
answer.append(abs(h-y))
answer.append(abs(w-x))
answer.append(abs(0-y))
answer.append(abs(0-x))
print(min(answer))