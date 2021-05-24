n, m = map(int, input().split())
x, y, direction = map(int, input().split())
# 2차원 리스트 컴프리헨션
d = [[0]*m for _ in range(n)]
d[x][y] = 1
array = []
# array로 입력받음
for _ in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while 1:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전 후 정면에 가보지 않는 칸 존재
    if array[nx][ny] == 0 and d[nx][ny] == 0:
        # 한번 갔던곳 체크용
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0 
        continue
    else:
        turn_time += 1

    # 4번 돌아도 다 갔던곳일때
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 가기전으로 돌아옴. 가능하면
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 못가는경우
        else:
            break
        turn_time = 0

print(count)





