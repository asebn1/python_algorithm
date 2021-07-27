def quickSort(s, low, high):
    if low < high:
        pivot = partition(s, low, high)
        quickSort(s, low, pivot-1)
        quickSort(s, pivot+1, high)
        
def partition(s, low, high):
    pivotpoint = s[low]
    j = low
    count1=0
    for i in range(low+1, high+1):
        if(s[i] < pivotpoint):
            j += 1
            swap(s,i,j)
            count1 = count1+1
            
    swap(s,low, j)
    print(count1)
    return j

def swap(s, num1, num2):
    s[num1], s[num2] = s[num2], s[num1]
    
s = [5,4,3,2,1]
quickSort(s,0,4)
print(s)
