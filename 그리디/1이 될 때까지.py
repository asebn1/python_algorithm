n, m = map(int, input().split())

cnt=0
while(1):
    if n==1:
        break

    if n%m==0:
        n /= m
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)
