x, y = 1, 1
move = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

a = int(input())
s = input().split()

for i in range(len(s)):
    for j in range(0, len(move)):
        if s[i] == move[j]:
            nx = x + dx[j]
            ny = y + dy[j]
    if nx < 1 or nx >= len(s) or ny < 1 or ny >= len(s):
        continue
    x = nx
    y = ny
print(x,y)