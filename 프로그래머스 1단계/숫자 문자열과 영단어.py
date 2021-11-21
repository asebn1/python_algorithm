def solution(s):
    lists = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(10):
        if lists[i] in s:
            print(lists[i])
            s=s.replace(lists[i], str(i))
    return int(s)