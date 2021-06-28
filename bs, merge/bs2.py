class Data():
    data = []
    def __init__(self, data, n):
        for i in range(n):
            self.data.append(data[i])
        self.n=n
        print(self.data)
        
    def binsearch(self,item, low, high):
        if(low>high):
            return -1;
        else:
            mid = (low+high)//2
            if(item == self.data[mid]):
                return mid
            elif item < self.data[mid]:
               return self.binsearch(item, low, mid-1)
            else:
               return self.binsearch(item, mid+1, high)


n=10
data = Data([1,3,5,6,7,9,10,14,17,19],n)
num=int(input("입력 : "))
location=data.binsearch(num,0,n-1)
print("위치 : %d" %location)
