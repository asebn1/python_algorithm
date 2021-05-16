n = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

mins = int(1e9)
maxs = -int(1e9)
def dfs(i, result, add, sub, mul, div):
    global mins, maxs
    # print(mins, maxs, result)
    if i == n:
        mins = min(mins, result)
        maxs = max(maxs, result)
        return
    if add:
        dfs(i+1, result+nums[i], add-1, sub, mul, div)
    if sub:
        dfs(i+1, result-nums[i], add, sub-1, mul, div)
    if mul:
        dfs(i+1, result*nums[i], add, sub, mul-1, div)
    if div:
        if result//nums[i] < 0:
            result = -(result)
            result = result//nums[i]
            result = -(result)
            dfs(i+1, result, add, sub, mul, div-1)
        else:
            dfs(i + 1, result//nums[i], add, sub, mul, div - 1)
dfs(1, nums[0], add, sub, mul, div)

print(maxs)
print(mins)
