n = int(input())
arr = []
for i in range(n):
    m = int(input())
    if m == 0:
        arr.pop()
    else:
        arr.append(m)

print(sum(arr))