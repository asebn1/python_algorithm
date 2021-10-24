def solution(n,a,b):
    answer = 0
    while 1:
        if a==b:
            break
        # 짝수로 변경
        if a%2 == 1:
            a += 1
        if b%2 == 1:
            b += 1
        a /= 2
        b /= 2
        answer += 1

    return answer

"""
1~N명 -> 토너먼트
12/34/56 -> 1234 -> ... -> 1
4 -> 2 -> 1 -> 1
7 -> 4 -> 2 -> 1
"""