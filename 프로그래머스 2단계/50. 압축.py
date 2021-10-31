def solution(msg):
    answer = []
    #사전
    dic = []
    for i in range(0, 26):
        dic.append(chr(65+i))

    # 끝 위치
    r = 0
    for i in range(0, len(msg)):
        for j in range(r+1, len(msg)+1):
            # 사전에 없으면 추가
            if msg[r:j] not in dic:
                answer.append(dic.index(msg[r:j-1])+1)
                dic.append(msg[r:j])
                r += j-r-1
                break
    answer.append(dic.index(msg[r:])+1)
    return answer