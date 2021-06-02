n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

def parent_find(parent, x):
    if parent[x] != x:
        parent[x] = parent_find(parent, parent[x])
    return parent[x]

def parent_union(parent, a, b):
    a = parent_find(parent, a)
    b = parent_find(parent, b)
    if a > b :
        parent[a] = b
    else:
        parent[b] = a

for i in range(m):
    w, a, b = map(int, input().split())
    if w == 0:
        # 합치기
        parent_union(parent, a, b)
    if w == 1:
        # 여부
        if parent_find(parent, a) == parent_find(parent, b):
            print("YES")
        else:
            print("NO")