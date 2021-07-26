
def prod(a, b):
    t = 4

    n1 = len(str(a))
    n2 = len(str(b))
    if (n1>n2):
        n = n1
    else:
        n = n2

    if(a==0 or b==0):
        return 0
    elif n<t:
        return a*b
    else:
        m = int(n/2)
        x = int(a/(10**m))
        y = a % (10**m)
        w = int(b / (10**m))
        z = b % (10**m)
        r = prod(x+y,w+z)
        p = prod(x,w)
        q = prod(y,z)
        return (p*(10**(2*m))) + ((r-p-q)*(10**m)) + q
    return 0
 
a = 1234567812345678
b = 2345678923456789

print(prod(a,b))
print(a*b)
