import sys

sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, sys.stdin.readline().split())))
    
zeroList = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeroList.append((i, j))

# [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), ... ]

def sudokuCk(x, y, i):
    for a in range(9):
        if sudoku[y][a] == i:
            return False

    for a in range(9):
        if sudoku[a][x] == i:
            return False

    yw, xw = y//3 * 3, x//3 * 3
    for a in range(3):
        for b in range(3):
            if sudoku[yw + a][xw + b] == i:
                return False

    return True



def dfs(n):
    if n == len(zeroList):
        for i in range(9):
            print(*sudoku[i])
        exit(0)

    for i in range(1, 10):
        y, x = zeroList[n]

        if sudokuCk(x, y, i):
            sudoku[y][x] = i
            dfs(n + 1)
            sudoku[y][x] = 0

dfs(0)