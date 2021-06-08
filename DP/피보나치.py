# 1.재귀
# #반복적으로 호출되는 것이 많다
def fibo_1(x):
    if x==1 or x==2:
        return 1
    return fibo_1(x-1) + fibo_1(x-2)

print(fibo_1(10))

# 리스트 사용
# 반복 호출 없음
d = [0] * 100
def fibo_2(x):
    if x==1 or x==2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo_2(x-1) + fibo_2(x-2)
    return d[x]
print(fibo_2(10))