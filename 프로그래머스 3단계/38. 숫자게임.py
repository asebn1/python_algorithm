def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=True)
    cnt = 0
    j = 0
    for i in range(len(A)):
        if B[j] > A[i]:
            cnt += 1
            j+= 1
        else:
            continue
    # print(A, B)
    return cnt