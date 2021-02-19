def solution(n):
    cnt = str(format(n, 'b')).count('1')
    while 1:
        n += 1
        new_cnt = str(format(n, 'b')).count('1')
        if cnt == new_cnt:
            return n