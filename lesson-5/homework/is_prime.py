def is_prime(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=1
    print(s==1)
n=int(input())
is_prime(n)
