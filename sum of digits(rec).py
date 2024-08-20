def sumofdigits(num):
    if(num==0):
            return 0
    return((num%10)+sumofdigits(num//10))
n=int(input("enter a number"))
sum=sumofdigits(n)
print(sum)

             



    