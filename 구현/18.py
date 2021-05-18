import copy
# 사이즈, 나무수, k년
n, m, k = map(int, input().split())
s2d2 = []
for i in range(n):
    s2d2.append(list(map(int, input().split())))
# 트리의 양분
tree_amount = [[5]*n for i in range(n)]

# 트리의 나이
tree_db = {}


# 트리양분, 나이 초기화
for i in range(n):
    for j in range(n):
        tree_db[(i,j)] = []
for i in range(m):
    x,y,age = map(int, input().split())
    tree_db[(x-1, y-1)].append(age)

# 트리 나이순으로 정렬
def treeSort():
    for i in tree_db.keys():
        if len(tree_db[i]) > 1:
            tree_db[i].sort()
treeSort()
def spring():
    # 트리 정렬
    for i in tree_db.keys(): # i = (2,1)
        # 값이 1개라도 있다면
        # 양분
        x, y = i
        value = 0
        new_tree = []
        if len(tree_db[i]) > 0:
            for j in tree_db[i]: # 3,4..
                if j <= tree_amount[x][y]:
                    new_tree.append(j+1)
                    tree_amount[x][y] -= j
                else:
                    value += j//2
            tree_db[i] = copy.deepcopy(new_tree)
        tree_amount[x][y] += value
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]
def fall():
    for i in tree_db.keys(): # i = (2,1)
        # 5가 속해 있으면
        if len(tree_db[i]) > 0:
            five_num = 0
            for j in tree_db[i]:
                if j % 5 == 0 and j != 0:
                    five_num += 1
            if five_num == 0:
                continue

            x, y = i
            # 번식
            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]
                if not (0<=nx<n and 0<=ny<n):
                    continue
                tree_db[(nx, ny)] = [1]*five_num + tree_db[(nx, ny)]

def winter():
    for i in range(n):
        for j in range(n):
            tree_amount[i][j] += s2d2[i][j]



age = 0
while 1:
    if age==k:
        break
    spring()
    fall()
    winter()
    age+=1
ret = 0
for i in tree_db.keys():
    ret += len(tree_db[i])

print(ret)