
import math
def kknum(num):
    orgnum=num
    rsum=0
    while(num!=0):
        rem=num%10
        remfact=math.factorial(rem)
        rsum+=remfact
        num=num//10
    if(rsum==orgnum):
        return True
    return False
num=int(input("enter the no to check "))
if kknum(num):
    print("krishnamurthy no")
else:
    print("not krishnamurthy no")