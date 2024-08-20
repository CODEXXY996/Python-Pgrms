n = int(input("Enter a number: "))
sum = 0
cpy = n
while(n > 0):
    r = n % 10
    sum = sum + (r*r*r)
    n = n // 10
if(sum == cpy):
    print("Armstrong number")
else:
    print("Not an Armstrong number")

