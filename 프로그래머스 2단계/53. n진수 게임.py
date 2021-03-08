import string
tmp = string.digits+string.ascii_lowercase

def solution(n, t, m, p):
    str1 = ''
    answer = ''
    # n진수 변환
    for i in range(0, t*m):
        str1 += convert(i, n)
    str1 = str1.upper()

    # m, p 적용
    cnt = 0
    for i in range(0, len(str1)):
        cnt += 1
        if cnt == p:
            answer += str1[i]
        if cnt == m:
            cnt = 0

    return answer[0:t]

# n진수 변환
def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]