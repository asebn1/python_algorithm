import queue

class Node:
        def __init__(self,level,weight,profit,bound,include):
                self.level = level
                self.weight = weight
                self.profit = profit
                self.bound = bound
                self.include = include
        def __cmp__(self, other):
               return cmp(self.bound, other.bound)

def kp_Best_FS():
        global maxProfit
        global bestset
        temp = n*[0]
        v = Node(-1,0,0,0.0,temp)

        v.bound = compBound(v)
        print("A", -v.bound)
        q = queue.PriorityQueue()
        q.put((v.bound,v))
        while not q.empty():
                v.bound, v = q.get()
                print("B",-v.bound)
                if v.bound < maxProfit:
                        u = Node(0,0,0,0.0,temp)
                        u.level = v.level+1
                        u.weight = v.weight + w[u.level]
                        u.profit = v.profit + p[u.level]
                        u.include = v.include[:]
                        u.include[u.level] = 1
                        u.bound = compBound(u)
                        print("level include profit bound ", u.level, u.include, u.profit, -u.bound)
                        if u.weight <= W and u.profit > maxProfit:
                                maxProfit = -u.profit
                                bestset = u.include[:]
                        if u.bound < maxProfit:
                                q.put((u.bound, u))
                        u = Node(0,0,0,0.0,temp)
                        u.weight = v.weight
                        u.profit = v.profit
                        u.include = v.include[:]
                        u.level = v.level+1
                        u.bound = compBound(u)
                        print("--level include profit bound ", u.level, u.include, u.profit, -u.bound)
                        if u.bound < maxProfit:
                                q.put((u.bound, u))


def compBound(u):
        if u.weight >= W:
                return 0
        else:
                result = u.profit
                j = u.level+1
                totweight = u.weight
                while j<=n-1 and totweight + w[j] <= W:
                        totweight += w[j]
                        result += p[j]
                        j+=1
        k=j
        if k<=n-1:
                result += (W-totweight)*p[k]/w[k]
        return -result

# heap??? minheap?????? bound??? ???????????? -??? ?????? ????????????. ????????? < maxProfit?????? ????????????.
n=4
W=16
p=[40,30,50,10]
w=[2,5,10,5]
include=[0]*n
maxProfit =0
bestset=n*[0]
kp_Best_FS()
print(bestset)
print(-maxProfit)
