n = int(input())
arr = list(map(int, input().split()))
d = [0] * (n)
result = -1001
for i in range(n):
    d[i] = max(d[i-1]+arr[i], arr[i])
    result = max(result, d[i])
print(d)  
print(result)