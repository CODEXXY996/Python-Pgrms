import random
print('number guessing game:')
target = random.randint(1,10)
print('target =',target)
n = int(input('Enter a number between 1 and 10'))
Flag = 0
if(n != target):
    while(True):
        n_update = int(input('Retry'))
        if n_update > target:
            print('Too high')
        elif n_update < target:
            print('Too less')
        else:
            Flag = 1
            break
else:
    print('Correct')
if Flag == 1:
    print('Correct')