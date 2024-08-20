no = int(input("Enter the number: "))
if no > 1:
    for i in range(2, no):
        if (no % i) == 0:
            print(str(no) + " is not a prime number")
            break
    else:
        print(str(no) + " is a prime number")
else:
    print(str(no) + " is not a prime number")
