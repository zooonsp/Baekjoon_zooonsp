n,m=map(int,input().split())

chessBoard=[]
cnt=[]

for i in range(n):
    chessBoard.append(input())
    
for a in range(n - 7):
    for b in range(m - 7):
        che_w = 0 # 흰색으로 시작했을 때 체크할 변수
        che_b = 0 # 검은색으로 시작했을 때 체크할 변수
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0: # 좌표의 합이 짝수일 때
                    if chessBoard[i][j] != 'W': # B라면
                        che_w += 1 # 흰색으로 시작한 변수이기에 짝수일 때 W가 와야함
                    else: # W라면
                        che_b += 1 # 검은색으로 시작한 변수이기에 짝수일 때 B가 와야함 
                else: # 좌표의 합이 홀수일 때
                    if chessBoard[i][j] != 'W': # B라면
                        che_b += 1 # 시작이 B로 시작했기에 W로 바꿔줘야함
                    else:
                        che_w += 1 
        cnt.append(che_w) 
        cnt.append(che_b) 
print(min(cnt))