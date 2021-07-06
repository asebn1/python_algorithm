s=[3,2,5,7,1,9,4,6,8]
n = len(s)

for i in range(0,n-1):
    min = i
    for j in range(i+1,n):
        if s[min] > s[j]:
            min = j
    temp = s[min]
    s[min] = s[i]
    s[i] = temp
           
print(s)
