n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

# 그래프 저장
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


friend_and = []
# 친구의 친구 저장
for i in graph[1]: # 2 3
    for j in graph[i]:
        friend_and.append(j)

# 합친 후 set
result = graph[1] + friend_and
result = list(set(result))

# 자기자신 - 1
if len(result) == 0:
    print(0)
else:
    print(len(result)-1)