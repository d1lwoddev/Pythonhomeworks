def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i ,"is a factor of ",n)
n=int(input())
factors(n)
