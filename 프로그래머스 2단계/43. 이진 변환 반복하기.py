def solution(s):
    cnt = 0
    zero = 0
    while 1:
        # 1. 2진변환
        cnt += 1
        zero += s.count('0')
        s = s.replace('0', '')
        # 2. 개수
        n = len(s)
        # 3. 결과
        s = str(format(n, 'b'))
        if s == '1':
            break
    return [cnt, zero]