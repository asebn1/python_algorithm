def solution(s):
    answer = ''
    temp = s.lower()
    lst = temp.split(' ')

    for i in range(len(lst)):
        lst[i] = lst[i].capitalize()

    answer = ' '.join(lst)

    return answer