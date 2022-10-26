from itertools import permutations
import sys

input = sys.stdin.readline
n = int(input())

l = list(map(int, input().split()))
operators = list(map(int, input().split()))
op = []
for i in range(operators[0]):
    op.append("+")

for i in range(operators[1]):
    op.append("-")

for i in range(operators[2]):
    op.append("*")

for i in range(operators[3]):
    op.append("/")

operators.clear()
for i in permutations(op, len(op)):
    operators.append(i)

vl = []
for i in range(len(operators)):
    value = l[0]
    for j in range(n - 1):
        if operators[i][j] == "+":
            value += l[j + 1]
        elif operators[i][j] == "-":
            value -= l[j + 1]
        elif operators[i][j] == "*":
            value *= l[j + 1]
        elif operators[i][j] == "/":
            if value < 0:
                value = -(abs(value) // l[j + 1])
            else:
                value = value // l[j + 1]
    vl.append(value)
print(max(vl))
print(min(vl))