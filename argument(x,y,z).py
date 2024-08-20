import math
def spectrum(x,y,z):
    if((x+y)>z):
        root=math.sqrt((x**2)+(y**2))
        return root
    return -1

x=int(input("enter the value of the x: "))
y=int(input("enter the value of y: "))
z=int(input("enter the value of z: "))

result= spectrum(x,y,z)
print("the output is",result)
      
