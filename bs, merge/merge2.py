def mergeSort2(s, low, high):
    if(low < high):
        mid = int((low+high)/2)
        mergeSort2(s, low, mid)
        mergeSort2(s, mid+1, high)
        merge2(s, low, mid, high)

def merge2(s, low, mid, high):
    u = [0]*(high-low+1)
    i = low
    j = mid+1
    k = 0
    
    while(i<= mid and j<= high):
        if(s[i] < s[j]):
            u[k] = s[i]
            i += 1
        else:
            u[k] = s[j]
            j += 1
        k += 1
    if(i>mid):
        for a in range(j,high+1):
            u[k] = s[a]
            k += 1
    else:
        for a in range(i,mid+1):
            u[k] = s[a]
            k += 1
    for a in range (low,high+1):
        s[a] = u[a-low]

    
s=[3,5,2,9,10,14,4,8]
mergeSort2(s,0,7)
print(s)
