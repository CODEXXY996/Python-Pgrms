n=int(input("enter the no"))
sum=0
if(n>0):
    r=n%10
    sum=sum+r
    n=n//10
    print(sum)
