import math


def solution(progresses, speeds):
    answer = []
    temp = progresses[:]
    for i in range(0, len(temp)):
        temp[i] = 100 - temp[i]
    for i in range(0, len(temp)):
        temp[i] = math.ceil(temp[i] / speeds[i])
    for i in range(0, len(temp) - 1):
        if temp[i] > temp[i + 1]:
            temp[i + 1] = temp[i]
    if temp[0] > 0:
        answer.append(1)
        if len(temp) == 1:
            return answer
    count = 0
    for i in range(0, len(temp) - 1):
        if temp[i] == temp[i + 1]:
            answer[count] += 1
        else:
            count += 1
            answer.append(1)

    return answer