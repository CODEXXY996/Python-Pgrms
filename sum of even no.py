n=int(input("enter the no"))
sum=0
print("enter the ",n,"numbers")
for i in range(n):
    sum=int(input())
if(n%2==0):
    sum=sum+n
print("sum of even no",sum)
