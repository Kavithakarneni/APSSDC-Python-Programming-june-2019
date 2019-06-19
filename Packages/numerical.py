def isprime(n):
    count=0
    for i in range(1,n+1):
        if n%i==0 and n%1==0:
            count=count+1
            print(count)
    if count==2:
        return True
    else:
        return False