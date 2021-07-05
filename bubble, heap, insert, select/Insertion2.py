class List():

    def __init__(self, s):
        self.data = s[:]
        self.n = len(s)

    def insertion_sort(self):
        for i in range(1,self.n):
            x = self.data[i]
            j = i-1
            while j>=0 and self.data[j]>x:
                self.data[j+1] = self.data[j]
                j-=1
            self.data[j+1] = x
        return self.data
        
s=[3,2,5,7,1,9,4,6,8]

a = List(s)
print(a.insertion_sort())
