def solution(s):
    board = list(map(int, s.split(' ')))

    return str(min(board)) + " " + str(max(board))