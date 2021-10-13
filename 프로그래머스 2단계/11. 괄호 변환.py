# u, v로 분리
def UVreturn(w):
    left = 0
    right = 0
    for i in range(len(w)):
        if w[i] == '(':
            left += 1
        if w[i] == ')':
            right += 1
        if left == right:
            return w[0:i+1], w[i+1:]

# u의 올바른 문자열 판단
def proper(u):
    left = 0
    right = 0
    for i in range(len(u)):
        if u[i] == '(':
            left += 1
        if u[i] == ')':
            right += 1
        if left < right:
            return False
    return True


def solution(p):
    answer = ''
    # 1
    if p == '':
        return ''

    # 2
    u, v = UVreturn(p)

    # 3
    if proper(u):
        # 3-1
        return u + solution(v)
    # 4
    else:
        # 4-1
        answer = '('
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ')'
        # 4-4
        for i in u[1:-1]:
            if i == ')':
                answer += '('
            else:
                answer += ')'
        return answer