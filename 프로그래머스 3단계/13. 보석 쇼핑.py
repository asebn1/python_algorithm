def solution(gems):
    answer = []
    setlen = len(set(gems))
    gemdict = {}
    start, end = 0, 0
    sect = len(gems) + 1

    while end < len(gems):
        if gems[end] not in gemdict:
            gemdict[gems[end]] = 1
        else:
            gemdict[gems[end]] += 1
        end += 1

        if len(gemdict) == setlen:  # 범위안에 모든 보석 존재할 때
            while start < end:
                if gemdict[gems[start]] > 1:
                    gemdict[gems[start]] -= 1
                    start += 1
                elif end - start < sect:
                    sect = end - start
                    answer = [start + 1, end]
                    break
                else:
                    break
    return answer