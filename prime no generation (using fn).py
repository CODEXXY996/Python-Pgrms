def checkPrime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    else:
        return False

limit = int(input("Enter the limit: "))
count = 0
num = 2
while count != limit:
    if checkPrime(num):
        print(num, end=" ")
        count += 1
    num += 1

