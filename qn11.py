import random
import string
s2 = list(string.digits)
random.shuffle(s2)
random.seed(0)
list_x = ['black','red','orange','peach']
list_y = s2+list_x
print(list_y)