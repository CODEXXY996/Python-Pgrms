import math
def is_prime(n):
    log = int(math.isqrt(n))
    console = math.isqrt(n)
    c = 0
    for key in range(3,log+1):
        if n%key == 0:
            if(n%log ==0):
                c = c+1
                break
    print('c=',c)
    if c ==0:
        return True
    else:
        return False

integer =  int(input('Enter an integer'))
valid = is_prime(integer)
if valid == True:
    print('prime')
else:
    print('Not a prime number')
