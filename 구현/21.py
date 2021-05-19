from collections import defaultdict
R, C, M = map(int, input().split())
shark_db = defaultdict(list)
idx = -1
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(M):
    r,c,s,d,z = map(int, input().split())
    d -= 1
    if d == 2:
        d = 3
    elif d == 3:
        d = 2
    shark_db[(r-1,c-1)].append((z,d,s))
# print(shark_db)
# 낚시왕 이동 후 잡기
ret = 0
def fishing():
    global idx, ret
    idx += 1
    for i in range(0, C):
        # print((i, idx))
        if (i, idx) in shark_db.keys():
            size = shark_db[(i, idx)].pop()[0]
            ret += size
            break

def sharkMove():
    global shark_db
    new_db = defaultdict(list)
    for i in shark_db.keys():
        x, y = i
        if len(shark_db[i])==0:
            continue
        size, d, s = shark_db[i][0]

        # 새로운 위치
        for j in range(s): # 스피드
            # 방향 바뀜
            if not (0<= (x+dx[d])<R and 0<= (y+dy[d]) <C):
                if d == 0:
                    d = 1
                elif d == 1:
                    d = 0
                elif d == 2:
                    d = 3
                elif d == 3:
                    d = 2
            x += dx[d]
            y += dy[d]
        new_db[(x, y)].append((size, d, s))
    # 옮기기 겹치는 경우 크기 큰것만
    shark_db = defaultdict(list)
    for i in new_db.keys():
        if len(new_db[i]) > 0:
            if len(new_db[i]) == 1:
                shark_db[i].append(new_db[i][0])
            # 2개 이상
            else:
                new_db[i] = sorted(new_db[i], key=lambda x : (-x[0]))
                shark_db[i].append(new_db[i][0])

for i in shark_db.keys():
    if len(shark_db[i]) > 1:
        shark_db[i] = sorted(shark_db[i], key=lambda x : (-x[0]))
        shark_db[i] = []
        shark_db[i].append(shark_db[i][0])
for i in range(C):
    fishing()
    sharkMove()
    # for i in shark_db.keys():
    #     x, y = i
    #     print(x+1, y+1, shark_db[i])
    # print()
print(ret)