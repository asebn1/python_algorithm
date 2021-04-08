import re


def solution(files):
    answer = []

    array = []
    # 2차원 리스트로 저장
    for i in range(len(files)):
        for j in range(len(files[i])):
            if ord((files[i])[j]) >= ord('0') and ord((files[i])[j]) <= ord('9'):

                # number 최대 5개
                cnt = 0
                for k in range(j, len(files[i])):
                    if ord((files[i])[k]) >= ord('0') and ord((files[i])[k]) <= ord('9'):
                        cnt += 1
                    else:
                        break
                    if cnt == 5:
                        break
                # head, number, tail 순서
                array.append([(files[i])[0:j], (files[i])[j:j + cnt], (files[i])[j + cnt:]])
                break

    # temp = [re.split(r"([0-9]+)", s) for s in files]
    array.sort(key=lambda x: (x[0].lower(), (int(x[1]))))

    # 합치기
    for i in range(len(array)):
        answer.append(array[i][0] + array[i][1] + array[i][2])
    return answer