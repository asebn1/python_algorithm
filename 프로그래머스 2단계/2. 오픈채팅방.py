def solution(record):
    answer = []
    # 3개로 나눈 리스트
    temp1 = []
    temp = []
    # 확인한 id 모음 (최종이름)
    exist = {}

    # temp 입력
    # [['Enter', 'uid1234', 'Muzi'], ['Leave', 'uid1234'], ['Enter', 'uid1234', 'Prodo'], ['Enter', 'uid4567', 'Prodo'], ['Change', 'uid4567', 'Ryan']]
    for i in range(len(record)):
        temp1.append(record[i].split(' '))
        temp.append(record[i].split(' '))

    # 아이디 순으로 정렬
    # [['Enter', 'uid1234', 'Muzi'], ['Leave', 'uid1234'], ['Enter', 'uid1234', 'Prodo'], ['Enter', 'uid4567', 'Prodo'], ['Change', 'uid4567', 'Ryan']]
    temp.sort(key=lambda x: x[1])

    start = 0
    end = 0
    while 1:
        if start >= len(temp):
            break
        for i in range(start, len(temp)):
            if i + 1 == len(temp):
                end = i
                break
            elif (temp[i])[1] == (temp[i + 1])[1]:
                continue
            else:
                end = i
                break

        # exist 추가
        # {'uid1234': 'Prodo', 'uid4567': 'Ryan'}
        for k in range(end, start - 1, -1):
            if (temp[k])[0] == 'Change' or (temp[k])[0] == 'Enter':
                exist[(temp[k])[1]] = (temp[k])[2]
                break
        start = end + 1

    # answer 추가
    for i in range(len(temp1)):
        if (temp1[i])[0] == 'Enter':
            answer.append(str(exist[(temp1[i])[1]]) + "님이 들어왔습니다.")
        if (temp1[i])[0] == 'Leave':
            answer.append(str(exist[(temp1[i])[1]]) + "님이 나갔습니다.")

    return answer