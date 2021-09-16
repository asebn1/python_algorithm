from collections import deque


def solution(tickets):
    length = len(tickets)
    db = {}
    visited = {}
    # db에 값 넣기
    for i in tickets:
        start, end = i[0], i[1]
        # db
        if start not in db.keys():
            db[start] = [end]
        else:
            db[start].append(end)

    for i in db.keys():
        db[i].sort()

    def dfs():
        stack = ["ICN"]
        path = []  # 경로 저장
        while stack:
            print(stack)
            top = stack[-1]
            if top not in db.keys() or len(db[top]) == 0:
                path.append(stack.pop())
            else:
                stack.append(db[top].pop(0))
        return path[::-1]

    return dfs()


solution([["ICN", "B"], ["B", "ICN"], ["ICN", "A"], ["A", "D"], ["D", "A"]])