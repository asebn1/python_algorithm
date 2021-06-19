array = [7,5,9,0,3,1,6,2,4,8]
# 방법1
array.sort()
# 방법2
result = sorted(array)
print(result)

array2 = [('바나나', 2), ('사과', 5), ('당근', 3)]
array2.sort(key=lambda x: x[1])
print(array2)
