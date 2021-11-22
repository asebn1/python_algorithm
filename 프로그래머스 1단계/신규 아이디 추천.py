def solution(new_id):
    answer = ''

    # 1. 소문자
    new_id = new_id.lower()

    # 2. 알파벳, 숫자, - , _ , .
    for i in new_id:
        if ((ord(i)) >= ord('a') and (ord(i)) <= ord('z')) or (
                (ord(i)) >= ord('0') and (ord(i)) <= ord('9')) or i == '-' or i == '_' or i == '.':
            answer += i

    # 3. . 중복제거
    while 1:
        if '..' not in answer:
            break
        answer = answer.replace('..', '.')

    # 4. .가 처음이나 끝에 있다면 제거
    if len(answer) > 0:
        if answer[0] == '.':
            answer = answer[1:]

    if len(answer) > 0:
        if answer[-1] == '.':
            answer = answer[0:-1]

    # 5. 빈 문자열이라면 a 대입
    if len(answer) == 0:
        answer = 'a'

    # 6.
    # 1) 16자 이상이면 15자 제외한 나머지 제거.
    if len(answer) > 15:
        answer = answer[0:15]
    # 2) 제거 후 마침표가 끝에 위치하면 마침표 제거
    if answer[-1] == '.':
        answer = answer[0:-1]

    # 7. 2자 이하라면 3자까지
    if len(answer) <= 2:
        last = answer[-1]
        while 1:
            answer += last
            if len(answer) >= 3:
                break

    return answer