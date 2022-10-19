k = int(input())

directions = []
lengths = []
max_high = 0
max_width = 0
high_index = 0
width_index = 0
answer = 0
for i in range(6):
    x, y = map(int, input().split())
    directions.append(x)
    lengths.append(y)
    if x == 3 or x == 4:
        if y >= max_high:
            max_high = y
            high_index = i
    else:
        if y >= max_width:
            max_width = y
            width_index = i
if (high_index + 1) % 6 == width_index :
    min_high = max_high - lengths[(width_index + 1) % 6] # 작은 사각형 높이
    min_width = max_width - lengths[(high_index - 1) % 6]
    
else:
    min_high = max_high - lengths[(width_index - 1) % 6] # 작은 사각형 높이
    min_width = max_width - lengths[(high_index + 1) % 6]
answer = ((max_high * max_width) - (min_high * min_width)) * k
print(answer)