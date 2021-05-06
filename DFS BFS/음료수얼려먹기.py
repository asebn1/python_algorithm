n, m = map(int, input().split())
arr = [[0]*m for _ in range(n)]
for i in range(n):
    arr[i] = list(map(int, input()))

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if arr[x][y] == 1:
        return False
    if arr[x][y] == 0:
        arr[x][y] = 1
        dfs(x, y-1)
        dfs(x, y+1)
        dfs(x-1, y)
        dfs(x+1, y)
        return True

result = 0
for x in range(0, n):
    for y in range(0, m):
        if dfs(x,y) == True:
            result += 1

print(result)