def solution(s):
    answer = ""

    j = 0
    temp = []
    if len(s) == 1:
        min = 1
    else:
        min = 1001

    # 10문자열이면 5개까지
    for i in range(1, (len(s) // 2) + 1):
        # 문자열 분리 1,2,3.... 개로
        # 1 : ['a', 'a', 'b', 'b', 'a', 'c', 'c', 'c']
        # 2 : ['aa', 'bb', 'ac', 'cc']
        # 3 : ['aab', 'bac', 'cc']
        while (1):
            if j > len(s):
                j = 0
                break
            temp.append(s[j:j + i])
            j += i
        if temp[-1] == '':
            temp.pop()

        # 압축된 모습
        """
        1 : 2a2ba3c
        2 : aabbaccc
        3 : aabbaccc
        4 : aabbaccc
        """
        pivot = temp[0]
        cnt = 0
        for k in range(len(temp) - 1):
            if pivot == temp[k]:
                cnt += 1
                if pivot != temp[k + 1]:
                    if cnt == 1:
                        answer += pivot
                    else:
                        answer += str(cnt) + pivot
                    pivot = temp[k + 1]
                    cnt = 0
        cnt += 1
        if cnt == 1:
            answer += pivot
        else:
            answer += str(cnt) + pivot

        # 가장 작은 값 갱신
        if min > len(answer):
            min = len(answer)

        # 초기화
        answer = ""
        temp = []

    return min