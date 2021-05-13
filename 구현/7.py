
n = int(input())
t = [0]
p = [0]
dp = [0]*(n+5)
# 입력
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
for i in range(n, 0, -1):
    if i+t[i]-1 > n:
        dp[i] = dp[i+1]
        continue
    dp[i] = max(dp[i+t[i]]+p[i], dp[i+1])
    # print(i, t[i], i + t[i] - 1, p[i])
    # dp[i] = max()
# print(dp)
print(max(dp))
