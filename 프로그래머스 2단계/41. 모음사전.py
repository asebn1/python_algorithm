def solution(s):
    ret, v = 0, [781, 156, 31, 6, 1]
    for i in range(len(s)):
        ret += "AEIOU".find(s[i]) * v[i] + 1
    return ret