def file_opener(input_opener):
    global target
    target = input_opener.read()
    sentence()
    vowelsandconsonant()
    words()
def sentence():
    number_of_sent = []
    number_of_sent = target.split('.')
    print('the number of sentences is:',(len(number_of_sent)-1))
def vowelsandconsonant():
    vol = 0
    consonant = 0
    list_x = list(target)
    for var in list_x:
        if var in ('a', 'e', 'i', 'o', 'u'):
            vol = vol + 1
        elif var in ('A', 'E', 'I', 'O', 'U'):
            vol = vol + 1
        else:
            consonant = consonant + 1
    print('number of vowels is:',vol)
    print('number of consonant is:',consonant)
def words():
    word = 0
    strings = target.split()
    word = len(strings)
    print('the number of words is:',word)

value_input = input('Enter a sentence or paragraph')
console_write = open('sentence.txt','w')
console_write.write(value_input)
console_write.close()
console_open = open('sentence.txt','r')
file_opener(console_open)


