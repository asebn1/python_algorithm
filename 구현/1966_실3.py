from collections import deque
# 중요도 1~9
# 문서개수 N, 몇번째 인쇄? M
# 각 중요도

result = []
n = int(input())
for _ in range(n):
    a, m = map(int, input().split())
    arr = list(map(int, input().split()))
    test = sorted(arr)
    check = deque()
    find_num = 0
    for i in range(len(arr)):
        if i==m:
            check.append([arr[i],True])
            find_num = arr[i]
        else:
            check.append([arr[i],False])

    how_cnt = 0
    while 1:
        if find_num == test[-1]:
            break
        num, checking = check.popleft()  
        # 같은 숫자일 시 끝내기
        
        # 찾을 수보다 크면 queue
        if num == test[-1]:  # 9 9 
            test.pop()    
            how_cnt+=1
        else:
            check.append([num, checking])
            
    howlen_cnt = 0
    for i in range(len(check)):
        if check[i][0]==find_num and check[i][1]==True:
            how_cnt += (howlen_cnt+1)
            break
        elif check[i][0]==find_num and check[i][1]==False:
            howlen_cnt += 1
    result.append(how_cnt)
for i in result:
    print(i)