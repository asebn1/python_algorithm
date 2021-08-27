def solution(triangle):
    db = triangle[::-1]
    for i in range(len(db)-1):
        for j in range(len(db[i])-1):
            db[i+1][j] += max(db[i][j], db[i][j+1])
    return db[-1][-1]