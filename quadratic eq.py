import math

a = int(input("Enter  a: "))
b = int(input("Enter  b: "))
c = int(input("Enter  c: "))

if (a == 0):
    print("This is not a quadratic equation.")
else:
    d = b**2 - 4*a*c
    if (d > 0):
        print("Roots are real.")
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print("Root 1:", root1)
        print("Root 2:", root2)
    elif (d == 0):
        print("Roots are real and same.")
        root = -b / (2*a)
        print("Root:", root)
    else:
        print("Roots are complex.")
        real_part  = -b / (2*a)
        imag_part = math.sqrt(-d) / (2*a)
        print("Root 1:", complex(real_part, imag_part))
        print("Root 2:", complex(real_part, -imag_part))
