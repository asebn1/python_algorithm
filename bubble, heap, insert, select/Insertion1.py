s=[3,2,5,7,1,9,4,6,8]
n = len(s)

for i in range(1,n):
    x = s[i]
    j = i - 1
    while j>=0 and s[j]>x:
        s[j+1] = s[j]
        j-=1
    s[j+1] = x

print(s)
