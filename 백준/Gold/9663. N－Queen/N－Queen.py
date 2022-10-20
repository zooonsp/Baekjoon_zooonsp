import sys

N = int(sys.stdin.readline())
row = [0] * N
cnt = 0
visit = [False] * N

# Queen이 서로 공격할 수 없는 지 확인
def check(q):
  for i in range(q):
    if abs(row[q] - row[i]) == q - i: # 대각선에 Queen이 있는지 확인
      return False
  return True

# DFS로 방법으로 탐색
def dfs(q):
  global cnt
  if q == N:
    cnt += 1
    return
    
  for i in range(N): 
    if visit[i]: # 같은 열에 Queen이 있는가
      continue
    
    row[q] = i
    if check(q):
      visit[i] = True
      dfs(q + 1)
      visit[i] = False

dfs(0)
print(cnt)
