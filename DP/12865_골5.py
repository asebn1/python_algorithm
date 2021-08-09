# n, k= map(int, input().split())
# stuff = [[0, 0]]
# table = [[0] * (k+1) for _ in range(n+1)]

import sys

n, k= map(int, input().split())
stuff = [[0, 0]]
table = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n):
    a, b = map(int, input().split())
    if a > k:
        continue
    stuff.append([a,b])

for i in range(1, n+1):
    w = stuff[i][0]
    v = stuff[i][1]

    for j in range(1, k+1):
        if w > j:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = max(table[i-1][j-w]+v, table[i-1][j])
print(table)
print(table[n][k])


#냅색 문제 풀이
# for i in range(1, n + 1):
#     for j in range(1, k + 1):
#         weight = stuff[i][0] 
#         value = stuff[i][1]
       
#         if j < weight:
#             table[i][j] = table[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
#         else:
#             table[i][j] = max(value + table[i - 1][j - weight], table[i - 1][j])

# print(table[n][k])