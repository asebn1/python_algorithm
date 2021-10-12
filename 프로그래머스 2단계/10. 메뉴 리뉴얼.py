from itertools import combinations


def solution(orders, course):
    answer = []
    temp = []
    combi = []
    # temp
    # [['A', 'B', 'C', 'F', 'G'], ['A', 'C'], ['C', 'D', 'E'], ['A', 'C', 'D', 'E'], ['B', 'C', 'F', 'G'], ['A', 'C', 'D', 'E', 'H']]
    for i in range(len(orders)):
        temp.append(list(orders[i]))

    # 조합 저장
    """
    [('A', 'B'), ('A', 'C'), ('A', 'F'), ('A', 'G'), ('B', 'C'), ('B', 'F'), ('B', 'G'), ('C', 'F'), ('C', 'G'), ('F', 'G'), ('A', 'B', 'C'), ('A', 'B', 'F'), ('A', 'B', 'G'), ('A', 'C', 'F'), ('A', 'C', 'G'), ('A', 'F', 'G'), ('B', 'C', 'F'), ('B', 'C', 'G'), ('B', 'F', 'G'), ('C', 'F', 'G'), ('A', 'B', 'C', 'F'), ('A', 'B', 'C', 'G'), ('A', 'B', 'F', 'G'), ('A', 'C', 'F', 'G'), ('B', 'C', 'F', 'G'), ('A', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'E'), ('C', 'D', 'E'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('C', 'D'), ('C', 'E'), ('D', 'E'), ('A', 'C', 'D'), ('A', 'C', 'E'), ('A', 'D', 'E'), ('C', 'D', 'E'), ('A', 'C', 'D', 'E'), ('B', 'C'), ('B', 'F'), ('B', 'G'), ('C', 'F'), ('C', 'G'), ('F', 'G'), ('B', 'C', 'F'), ('B', 'C', 'G'), ('B', 'F', 'G'), ('C', 'F', 'G'), ('B', 'C', 'F', 'G'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'H'), ('C', 'D'), ('C', 'E'), ('C', 'H'), ('D', 'E'), ('D', 'H'), ('E', 'H'), ('A', 'C', 'D'), ('A', 'C', 'E'), ('A', 'C', 'H'), ('A', 'D', 'E'), ('A', 'D', 'H'), ('A', 'E', 'H'), ('C', 'D', 'E'), ('C', 'D', 'H'), ('C', 'E', 'H'), ('D', 'E', 'H'), ('A', 'C', 'D', 'E'), ('A', 'C', 'D', 'H'), ('A', 'C', 'E', 'H'), ('A', 'D', 'E', 'H'), ('C', 'D', 'E', 'H')]
    """
    for i in range(len(temp)):
        temp[i].sort()
        for j in course:
            for k in list(combinations(temp[i], j)):
                combi.append(k)

    # 집합 형태 저장 후 다시 리스트( 중복 제거 )
    combiSet = set(combi)
    combiSet = list(combiSet)
    combiSet.sort()
    # count 셈
    combiDict = {}
    for i in range(len(combiSet)):
        if combi.count(combiSet[i]) >= 2:
            combiDict[combiSet[i]] = combi.count(combiSet[i])

    combiDict = sorted(combiDict.items(), key=lambda x: -x[1])

    # 정답 추리기
    tem = []
    for i in course:  # 2, 3, 4
        for j in range(len(combiDict)):
            if len(combiDict[j][0]) == i:
                tem.append(combiDict[j])
        if len(tem) > 0:
            max = tem[0][1]
            for k in range(len(tem)):
                if tem[k][1] == max:
                    answer.append(tem[k][0])
        tem = []
    # 문자열 변환
    # 전 [('A', 'D'), ('C', 'D'), ('A', 'C', 'D'), ('A', 'D', 'E'), ('X', 'Y', 'Z')]
    # 후 ['AD', 'CD', 'ACD', 'ADE', 'XYZ']
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
    answer.sort()
    return answer