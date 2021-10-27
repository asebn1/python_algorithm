from collections import deque
def alright(board):
    stack = []
    for i in board:
        if i == '[' or i == '{' or i == '(':
            stack.append(i)
        elif i == ']':
            if len(stack)==0:
                return False
            elif stack[-1] == '[':
                stack.pop()
        elif i == '}':
            if len(stack)==0:
                return False
            if stack[-1] == '{':
                stack.pop()
        elif i == ')':
            if len(stack)==0:
                return False
            if stack[-1] == '(':
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False

def solution(s):
    board = deque(list(s))
    result = 0
    result += alright(board)
    for i in range(len(s)-1):
        pop = board.popleft()
        board.append(pop)
        result += alright(board)
    return result