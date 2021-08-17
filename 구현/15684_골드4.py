n, l = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(arr[j][i])
    arr.append(temp)

cnt = 0
for i in arr:
    # 초기 
    check = 1
    height = i[0]
    bool_check = True
    for j in range(1, n):
        # 평지
        if i[j] == height:
            check += 1
        # 종료. 2개이상 차이
        elif i[j] > (height+1) or i[j] < (height-1): 
            bool_check = False
            break
        # 높아질 때
        elif i[j] == (height+1):
            # 여유분이 존재
            if check >= l:
                check = 1
                height = i[j]
            else:
                bool_check = False
                break
        # 낮아질 때
        elif i[j] == (height-1):
            if check >= 0:
                check = 1-l
                height = i[j]
            else:
                bool_check = False
                break

    if bool_check == True and check >= 0:
        cnt += 1
print(cnt)