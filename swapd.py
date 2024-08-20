def cyctem (**k):
    print('the original dictionary is:',k)
    list_x = [val for val in k.keys()]
    list_y = [console for console in k.values()]
    new_k = dict(zip(list_y,list_x))
    print('the swapper dictionary is:',new_k)
cyctem(a=1,b=2,c=3)