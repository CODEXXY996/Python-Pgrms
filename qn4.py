print('integer checker')
limit = int(input('enter limit'))
list_x =[]
pos = 0
neg = 0
xer = 0
for key in range(limit):
    var = int(input('enter value'))
    list_x.append(var)
for target in list_x:
    if target > 0:
        pos = pos+1
    elif target < 0:
        neg = neg+1
    else:
        xer = xer+1
print('Positive numbers:',pos)
print('Negative numbers:',neg)
print('Zeros:',xer)
