input()
l1 = set(list(map(int, input().split())))
l2 = set(list(map(int, input().split())))

a = l1 - l2
b = l2 - l1
print(len(a) + len(b))