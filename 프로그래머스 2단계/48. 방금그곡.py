def solution(m, musicinfos):
    answer = '(None)'
    time = []
    name = []
    data = []
    location = []
    for i in range(0, len(musicinfos)):
        # 1. 데이터 입력 받음
        data1, data2, data3, data4 = musicinfos[i].split(',')
        # 2. 데이터 별로 저장
        if data1[0:2] > data2[0:2]:
            data2 = str(int(data2[0:2]) + 24) + data2[2:]
        time.append((int(data2[0:2]) - int(data1[0:2])) * 60 + int(data2[3:5]) - int(data1[3:5]))
        name.append(data3)
        data.append(data4)

    # 위치
    result = []
    # 샾 변경
    m = m.replace('C#', 'Z')
    m = m.replace('D#', 'X')
    m = m.replace('F#', 'Q')
    m = m.replace('G#', 'W')
    m = m.replace('A#', 'R')
    for i in range(0, len(musicinfos)):
        data[i] = data[i].replace('C#', 'Z')
        data[i] = data[i].replace('D#', 'X')
        data[i] = data[i].replace('F#', 'Q')
        data[i] = data[i].replace('G#', 'W')
        data[i] = data[i].replace('A#', 'R')

    for i in range(0, len(musicinfos)):
        # 데이터 변경. 재생 시간에 맞게
        # 1. 재생시간 < 악보시간
        if time[i] < len(data[i]):
            data[i] = (data[i])[:time[i]]
        # 2. 재생시간 > 악보시간
        else:
            cnt = 0
            size = len(data[i])
            temp = data[i]
            data[i] = ''
            for j in range(0, time[i]):
                data[i] += temp[cnt]
                cnt += 1
                if cnt == size:
                    cnt = 0

    # m -> 악보 비교
    for i in range(0, len(musicinfos)):
        if m in data[i]:
            result.append(i)

    # 결과 1개일시 바로 리턴
    if len(result) == 1:
        answer = name[result[0]]
        return answer
        # 1개 이상일 때 가장 긴 시간 리턴
    elif len(result) > 1:
        # max
        m = -1
        lo = -1
        for i in result:
            if m < time[i]:
                m = time[i]
                lo = i

        if m == -1:
            return answer
        else:
            answer = name[lo]
    return answer