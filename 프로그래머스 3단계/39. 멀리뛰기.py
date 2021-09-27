def solution(n):
    dp = [0] *10000
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 2000):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n]