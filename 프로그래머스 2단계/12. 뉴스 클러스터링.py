import math


def solution(str1, str2):
    answer = 1

    array1 = []
    array2 = []

    # 겹치는 것 있으면 구분해주기 위함
    temp1 = [0] * (len(str1) - 1)
    temp2 = [0] * (len(str2) - 1)

    # 대소문자 구분X
    str1 = str1.upper()
    str2 = str2.upper()
    # 길이가 2 이상일때 리스트로 나눠 줌
    # str1
    if len(str1) >= 2:
        for i in range(len(str1)):
            if i + 2 <= len(str1):
                # A~Z 아니면 버림
                check1 = ord(str1[i])
                check2 = ord(str1[i + 1])

                # A~Z 라면 추가
                if check1 >= 65 and check1 <= 90 and check2 >= 65 and check2 <= 90:
                    # 넣을 때 겹치는 것 있으면 구분해줌
                    # AA / AA / AA -> AA / AA1 / AA2
                    if str1[i:i + 2] in array1:
                        # 이미 있는 개수 저장
                        cnt = array1.count(str1[i:i + 2])
                        array1.append(str1[i:i + 2])
                        temp1[i] += cnt
                    else:
                        array1.append(str1[i:i + 2])
                else:
                    array1.append(-1)

    # str2
    if len(str2) >= 2:
        for i in range(len(str2)):
            if i + 2 <= len(str2):
                check1 = ord(str2[i])
                check2 = ord(str2[i + 1])

                # A~Z 라면 추가
                if check1 >= 65 and check1 <= 90 and check2 >= 65 and check2 <= 90:
                    # 넣을 때 겹치는 것 있으면 구분해줌
                    # AA / AA / AA -> AA / AA1 / AA2 하기 위해
                    if str2[i:i + 2] in array2:
                        # 이미 있는 개수 저장
                        cnt = array2.count(str2[i:i + 2])
                        array2.append(str2[i:i + 2])
                        temp2[i] += cnt
                    else:
                        array2.append(str2[i:i + 2])
                else:
                    array2.append(-1)

    # AA / AA / AA -> AA / AA1 / AA2 변환 작업
    for i in range(len(str1) - 1):
        if temp1[i] != 0:
            array1[i] = array1[i] + str(temp1[i])
    for i in range(len(str2) - 1):
        if temp2[i] != 0:
            array2[i] = array2[i] + str(temp2[i])
    # 집합 변환
    array1 = set(array1)
    array2 = set(array2)
    # 집합 -1 제거
    if -1 in array1:
        array1.remove(-1)
    if -1 in array2:
        array2.remove(-1)

    checkAnd = len(array1 & array2)
    checkOr = len(array1 | array2)
    if checkOr == 0:
        answer = 1
    else:
        answer = checkAnd / checkOr
    answer *= 65536
    # 소수점 버림
    answer = math.trunc(answer)
    return answer