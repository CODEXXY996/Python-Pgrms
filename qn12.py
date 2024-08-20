import math
input_Value = int(input('enter limit'))
list_x = []
for key in range(input_Value):
    value = input('enter word')
    list_x.append(value)
half = round(len(list_x)/2)
print(half)
print(list_x[half::])