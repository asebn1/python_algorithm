
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
first = arr[-1]
secound = arr[-2]

answer = first * (m//k) * k
answer += secound * (m % k)

print(answer)