def invest(amount,rate,years):
    for i in range(1,int(years)+1):
        print("year ",i,": ",round(amount*(1+rate/100)**i,2))
amount,rate,years=map(float,input().split())
invest(amount,rate,years)        
