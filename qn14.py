def input_element():
    global list_x
    list_x = []
    limit = int(input('Enter limit of words'))
    for key in range(limit):
        value = input('Enter word')
        list_x.append(value)
    print('original list: ',list_x)
def check_element():
    global check_in
    check_in = input('enter the word to be removed')
    global flag
    flag = 0
    if check_in in list_x:
        flag = 1
def remove_element():
    if flag == 1:
        list_x.remove(check_in)
    else:
        print('element absent')
def display_list():
    print('The updated list is: ',list_x)

input_element()
check_element()
remove_element()
display_list()

