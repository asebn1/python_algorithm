def checktr(time,li):
    c=0
    start=time
    end=time+1000
    for i in li:
        if i[1] >= start and i[0] < end:
            c += 1
    return c
def solution(lines):
    start = []
    end = []
    time = []
    li = []
    for i in range(len(lines)):
        """ 리스트 추가 """
        # 걸린 시간 s 제거 추가
        time.append(int(float(lines[i].split()[2][:-1])*1000))
        # end 시간 추가
        endTemp = lines[i].split()[1]
        endTemp = int(endTemp[0:2])*60*60*1000+int(endTemp[3:5])*60*1000+int(float(endTemp[6:])*1000)
        end.append(endTemp)
        # start 시간 추가
        start.append(end[i]-time[i]+1)
        li.append([start[i], end[i]])
    # 리스트 1개일때 1개 반환
    if len(end) == 1:
        return 1

    # max 계산
    max1 = 1
    for i in li:
        max1 = max(max1,checktr(i[0],li),checktr(i[1],li))
    return max1