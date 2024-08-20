x=int(input("enter the value of x: "))
y=int(input("enter the value of y: "))
z=int(input("enter the value of z: "))

if(x<y)&(x<z):
    print(x,"is smaller")
elif(y<x)&(y<z):
    print(y,"is smaller")
elif(z<x)&(z<y):
    print(z,"is smaller")
