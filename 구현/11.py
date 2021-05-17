from itertools import combinations

n = int(input())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
members = [i for i in range(n)]
mins = int(1e9)


#조합으로 가능한 팀 생성해주기
possible_team = []
s = []
def dfs(start):
    if len(s) == n//2:
        possible_team.append(s.copy())
        return
    for i in range(start, n):
        if i in s:
            continue
        s.append(i)
        dfs(i+1)
        s.pop()
dfs(0)
# print(possible_team)
# print(possible_team)
for i in range(len(possible_team)//2):
    # A팀
    teamA = possible_team[i]  # 0 1 2
    scoreA = 0
    for j in range(len(teamA)):
        for k in range(len(teamA)):
            scoreA += board[teamA[j]][teamA[k]]
    # B팀
    teamB = possible_team[-i-1]
    scoreB = 0
    teamA = possible_team[i]  # 0 1 2
    for j in range(len(teamB)):
        for k in range(len(teamB)):
            scoreB += board[teamB[j]][teamB[k]]
    mins = min(mins, abs(scoreA-scoreB))
print(mins)
