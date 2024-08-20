def mark(value):
    if(value > 90 and value <= 100):
        return 'A'
    elif(value > 80 and value <= 89):
        return 'B'
    elif (value > 70 and value <= 79):
        return 'C'
    elif (value > 60 and value <= 69):
        return 'D'
    else:
        return 'F'

def subjects(console):
    global list_subject

    for i in range(console):
        sub_ject = input('Enter Subject {var}'.format(var = i+1))
        list_subjects.append(sub_ject)
    global list_grade
    for key in list_subjects:
        mar_ks = int(input('Enter marks for {sub}:'.format(sub = key)))
        grd = mark(mar_ks)
        list_grade.append(grd)
    mark_stog = dict(zip(list_subjects,list_grade))
    print(mark_stog)

limited = int(input('Enter number of subjects'))
list_grade = []
list_subjects = []
subjects(limited)
