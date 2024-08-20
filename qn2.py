print('Even or odd list')
limit = int(input('Enter limit'))
list_x = []
list_y = []
for i in range(limit):
    target = int(input('Enter value'))
    list_x.append(target)
for key in list_x:
    if key % 2 == 0:
        list_y.append('Even')
    else:
        list_y.append('Odd')
key_value = dict(zip(list_x,list_y))
print(key_value)