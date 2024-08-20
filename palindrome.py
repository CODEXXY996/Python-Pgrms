x=int(input("enter the no"))
rem=0
rev=0
cpy=x
while(x>0):
    rem=x%10
    rev=rev*10+rem
    x=x//10
if(cpy==rev):
    print("palindrome")
else:
    print("not plindrome")
    
