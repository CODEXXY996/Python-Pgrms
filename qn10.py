n = int(input('enter limit'))
list_x = []
for key in range(n):
    up = int(input('enter value'))
    list_x.append(up)
list_y = []
for key in list_x:
    list_y.append(key*2)
print(list_y)