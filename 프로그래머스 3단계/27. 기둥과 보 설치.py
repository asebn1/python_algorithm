import copy


def add(answer, x, y, a):
    # 기둥
    if a == 0:
        if y == 0:
            return 1
        elif [x, y - 1, a] in answer:
            return 1
        elif [x - 1, y, 1] in answer or [x, y, 1] in answer:
            return 1
        else:
            return 0
    # 보
    else:
        if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer:
            return 1
        elif [x - 1, y, a] in answer and [x + 1, y, a] in answer:
            return 1
        else:
            return 0


def delete(answer, x, y, a):
    temp = copy.deepcopy(answer)
    temp.remove([x, y, a])
    # 방법
    """
    5개중 1개 삭제 -> 4개
    4개를 새로 add했을 때 갯수가 4개가 맞으면 delete 가능
    """
    count = 0
    for i in temp:
        count += add(temp, i[0], i[1], i[2])

    if count == len(temp):
        return 1
    else:
        return 0


def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x, y, a, d = i[0], i[1], i[2], i[3]
        # 추가
        if d == 1:
            if add(answer, x, y, a):
                answer.append([x, y, a])
        # 삭제
        else:
            if delete(answer, x, y, a):
                answer.remove([x, y, a])
        answer.sort(key=lambda x: (x[0], x[1], x[2]))
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer