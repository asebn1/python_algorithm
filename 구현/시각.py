aba = int(input())
h, b, c = 0, 0, 0
cnt = 0
while(1):
    str1 = str(h)+str(b)+str(c)
    if str1 == str(aba)+'5959':
        break
    if '3' in str1:
        cnt += 1
    c += 1
    if c == 60:
        c = 0
        b += 1
    if b == 60:
        b = 0
        h += 1
print(cnt)
