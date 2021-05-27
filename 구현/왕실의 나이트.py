s = input()

x = ord(s[0])-96
y = int(s[1])
tip = (x, y)
cnt = 0
steps = [(2, 1), (2, -1),(-2, 1),(-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
temp = []
for i in range(0, 8):
    temp.append([tip[0]+steps[i][0], tip[1]+steps[i][1]])

for i in range(0, 8):
    if temp[i][0] > 0 and temp[i][1] > 0:
        cnt+=1

print(cnt)