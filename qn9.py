print('list creation and updation')
limit = int(input('Enter the number of your favourite fruits:'))
list_xy = []
for key in range(limit):
    fruit_input = input('Enter fruit {name}:'.format(name=key+1))
    list_xy.append(fruit_input)

print('The second element of the fruit list is:',list_xy[1])
list_xy[len(list_xy)-1] = 'Banana'
print('The updated list is',list_xy)