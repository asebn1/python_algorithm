import queue

class Node:
        def __init__(self,level,weight,profit,include):
                self.level = level
                self.weight = weight
                self.profit = profit
                self.include = include

def kp_BFS():
        global maxProfit
        global bestset
        
        q = queue.Queue()
        root = Node(-1,0,0,[])
        q.put(root)
        while not q.empty():
                v = q.get()
                v.include.append(1)
                t = v.include[:]
                ulevel = v.level+1
                u = Node(ulevel, v.weight+w[ulevel], v.profit+p[ulevel], t)
                if u.weight <= W and u.profit > maxProfit:
                        maxProfit = u.profit
                        bestset = u.include[:]
                if compBound(u) > maxProfit:
                        q.put(u)
                v.include.pop()
                v.include.append(0)
                t = v.include[:]
                include[ulevel] = 0
                u = Node(ulevel, v.weight, v.profit, t)
                if compBound(u) > maxProfit:
                        q.put(u)
        

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
        return result
        
n=4
W=16
p=[40,30,50,10]
w=[2,5,10,5]
include=[0]*n
maxProfit=0
bestset=n*[0]
kp_BFS()
print(bestset)
