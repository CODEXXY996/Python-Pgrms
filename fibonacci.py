limit=int(input("enter the limit:"))



print("the series is :")
a=0
b=1
sum=0
if(limit==1):
    print(a,end="")
elif(limit==2):
    print(a,b,end="")
else:
        print(a,b,end=" ")
        for i in range(2,limit+1):
            sum=a+b
            a=b
            b=sum
            print(sum,end= " ")
