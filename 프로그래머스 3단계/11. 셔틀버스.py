def solution(n, t, m, timetable):
    minutes = []
    first = 540     # 첫차시간
    answer = 0
    for time in timetable:      # 분단위 계산
        a = time.split(':')
        minute = int(a[0]) * 60 + int(a[1])
        minutes.append(minute)
    minutes.sort()    # 대기자 정렬

    for i in range(0, n):   # 버스 운행
        count = 0           # 다음차 대기자 수
        for j in range(0, len(minutes)):    # 대기자수 계산
            if minutes[j] <= (first + (i*t)):
                count += 1
                if count == m:
                    break

        if i == n-1:    # 막차
            if count >= m:
                answer = minutes[m-1] -1   # 막차마지막탑승
            else:
                answer = first + (i * t)   # 막차시간탑승
            break
        else:           # 앞차 대기자 탑승
            if count >= m:
                minutes[:m] = []    # 정원 채워서 보내기
            else:
                minutes[:count] = []    # 대기자수 만큼 보내기

    # str변환
    mok = answer//60
    na = answer%60
    if mok < 10:
        mok = '0' + str(mok)
    else :
        mok = str(mok)
    if na < 10:
        na = '0' + str(na)
    else:
        na = str(na)
    answer = mok + ':' + na
    return answer