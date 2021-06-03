
n, m = map(int, input().split())
arr = [ [0] * m for _ in range(n)]
minn = []
for i in range(0, n):
    arr[i] = list(map(int, input().split()))
    minn.append(min(arr[i]))

answer = max(minn)
print(answer)