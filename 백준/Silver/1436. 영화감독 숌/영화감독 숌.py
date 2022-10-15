n = int(input())
v = 666
c = 0

while True:
    if '666' in str(v):
        c += 1
    if c == n:
        print(v)
        break    
    v += 1