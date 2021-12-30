def sumOrProduct(n, q):
    s1=0
    n1=1
    if q==1:
        for i in range(1,n+1):
            s1=s1+i
        return s1
    elif q==2:
        for i in range(1,n+1):
            n1=n1*i
        return n1
print(sumorproduct(n,q))
