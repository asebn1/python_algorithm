db = []

for i in range(1, 10000):
    n = str(i)
    temp = i
    for i in n:
        temp += int(i)
    db.append(temp)

db.sort()

result = []
for i in range(1,10000):
    if i not in db:
        print(i)