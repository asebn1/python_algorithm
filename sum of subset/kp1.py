def kp(i, profit, weight):
        global bestset
        global maxp
               
        if(weight <= W and profit > maxp):
                maxp = profit
                bestset = include[:]
        if promising(i, weight, profit):
                include[i+1] = 1
                kp(i+1, profit+p[i+1], weight+w[i+1])
                include[i+1] = 0
                kp(i+1, profit, weight)

def promising(i,weight,profit):
    global maxp

    if weight >= W:
        return False
    else:
        #상태공간트리에서 $28 4 $53이라면 53 확인하기 위해서 사용
        j=i+1
        bound = profit
        totweight = weight
        while (j < n and totweight+w[j] <= W):
           totweight += w[j]
           bound += p[j]
           j += 1
        k = j
        if k < n:
           bound += (W-totweight)*(p[k]/w[k])
           
        return bound > maxp

n=4
W=16
p=[40,30,50,10]
w=[2,5,10,5]
maxp=0
include =[0,0,0,0]
bestset = [0,0,0,0]
kp(-1,0,0)
print(maxp)
print(bestset)
