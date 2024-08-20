no=int(input("enter the no"))
rev=0
while(no>0):
    r=no%10
    rev=rev*10+r
    no=no//10
print(rev)
