def solution(N, number):
    dp = [[]]
    for i in range(1, 9):
        temp = []
        for j in range(1, i):
            for k in dp[j]:
                for l in dp[i-j]:
                    # 더하기
                    temp.append(k+l)
                    # 빼기
                    if k-l>0:
                        temp.append(k-l)
                    if l-k>0:
                        temp.append(l-k)
                    # 곱하기
                    temp.append(l*k)
                    # 나누기
                    if l%k == 0 and k!=0:
                        temp.append(l//k)
                    if k%l == 0 and l!=0:
                        temp.append(k//l)
        temp.append(int(str(N)*i))
        if number in temp:
            return i
        dp.append(list(set(temp)))
    return -1
    # print(dp[:5])
"""
3 55 ...
1,2 dp 
dp[2] dp[1]
"""