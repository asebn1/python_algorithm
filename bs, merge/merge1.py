def mergeSort(n, s):
    h= int(n/2) ##두 개 분할
    m= n-h
    
    if(n>1):
        u = s[:h]
        v = s[h:]
        mergeSort(h,u)
        mergeSort(m,v)
        merge(h,m,u,v,s)
        
def merge(h,m,u,v,s):
    i=j=k=0
    while(i<= h-1 and j<= m-1):
        if(u[i] < v[j]):
            s[k] = u[i]
            i += 1
        else:
            s[k] = v[j]
            j += 1
        k += 1
    if(i>h-1):
        for a in range(j, m):
            s[k] = v[a]
            k += 1
    else:
        for a in range(i, h):
            s[k] = u[a]
            k += 1

    
s=[3,5,2,9,10,14,4,8]
mergeSort(8,s)
print(s) 
