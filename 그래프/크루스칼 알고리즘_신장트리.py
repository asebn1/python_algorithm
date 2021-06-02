# 신장트리 : 1) 모든 노드를 포함하면서, 2) 사이클이 존재하지 않는 부분그래프
# 사용법
""" 
1. 간선 데이터 : 비용에 따라 [오름차순] 정렬
2. 현재 간선이 사이클 발생하는지 여부 확인      ->  서로소 집합 알고리즘 사용!  (union을 통해 동일한 집합인지 확인)
    - 사이클 발생 x    :    신장트리 포함
    - 사이클 발생 o    :    신장트리 포함 x
3. 모든 간선 2번 반복
"""
def find_parent(parent, x):
    # 루트노드가 아니면 루트 나올때까지 재귀호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 노드의 개수, 간선의 개수
v, e = 7, 9
parent = [0] * (v+1)

# 부모 자기자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 모든 간선 정보 입력받기
edges = []
# e번 9번
edges.append((1, 2, 29))
edges.append((1, 5, 75))
edges.append((2, 3, 35))
edges.append((2, 6, 34))
edges.append((3, 4, 7))
edges.append((4, 6, 23))
edges.append((4, 7, 13))
edges.append((5, 6, 53))
edges.append((6, 7, 25))

# 비용 순으로 정렬
edges.sort(key = lambda x : x[2])

result = 0

for edge in edges:
    a, b, cost = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)