def solution(operations):
    result = []
    q = []
    for i in operations:
        a, b = i.split()
        b = int(b)
        if a == 'I':
            q.append(b)
        elif a == 'D':
            if b == 1:
                if len(q) > 0:
                    q.sort()
                    result.append(q.pop())
            elif b == -1:
                if len(q) > 0:
                    q.sort()
                    result.append(q.pop(0))
    if len(q) == 0:
        return [0,0]
    else:
        return [max(q), min(q)]