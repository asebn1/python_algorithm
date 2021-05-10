n = int(input())
board = list(map(int, input().split()))
b, c = (map(int, input().split()))

answer = 0
for i in board:
    num = i

    # 총감독관
    num -= b
    answer += 1
    if num <= 0:
        continue
    else:
        # 부감독관
        if int(num)== (num//c)*c:
            answer += num//c
        else:
            answer += num // c + 1
    # print(answer)
print(answer)