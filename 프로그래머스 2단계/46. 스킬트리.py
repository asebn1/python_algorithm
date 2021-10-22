def solution(skill, skill_trees):
    cnt = 0
    for i in skill_trees:
        # 각 위치
        temp = ''
        nothing = 0
        for j in i:
            if j in skill:
                temp += j
            else:
                nothing += 1
        if len(temp) > 0 and temp[0] == skill[0] and temp in skill:
            cnt += 1
        if nothing == len(i):
            cnt += 1
    return cnt
# print(solution("CBD", ["C", "D", "CB", "BDA"]))
"""
CB / CXYB / AEX / IJCB
선행스킬 1->2->3
1->%->2->^->3
"""