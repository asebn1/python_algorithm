from collections import deque
n = int(input())
k = int(input())
visited = [[False]*n for _ in range(n)]
# 사과위치
for i in range(k):
    a, b = map(int, input().split())
    visited[a-1][b-1] = True
# print(visited)
# 변환
db = {}
l = int(input())
for i in range(l):
    a, b = map(str, input().split())
    db[int(a)] = b
# print(db)

count = 0
d = 3 # 방향
body = deque()
headx = 0
heady = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while 1:
    # print(headx, heady, count, body, d)
    if (count) in db.keys():
        if d == 3:
            d = 1 if db[count]=='D' else 0
        elif d == 2:
            d = 0 if db[count]=='D' else 1
        elif d == 1:
            d = 2 if db[count]=='D' else 3
        elif d == 0:
            d = 3 if db[count]=='D' else 2
    count += 1
    # 값 초과
    if not (0<= headx+dx[d] < n and 0<=heady+dy[d]<n):
        print(count)
        break

    # 꼬리 닿음
    if [headx + dx[d], heady+dy[d]] in body:
        print(count)
        break

    # 다음번에 사과가 있다면
    if visited[headx+dx[d]][heady+dy[d]]:
        visited[headx + dx[d]][heady + dy[d]] = False
        body.appendleft([headx, heady])
        headx += dx[d]
        heady += dy[d]
    else:
        if len(body) == 1:
            body[0][0] = headx
            body[0][1] = heady
        elif len(body) > 1:
            body.pop()
            body.appendleft([headx, heady])
        headx += dx[d]
        heady += dy[d]

    # if count == 20:
    #     break
