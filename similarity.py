def eq_strings(s1, s2):
    l1 = list(s1)
    l2 = list(s2)
    flag = 1

    if len(l1) == len(l2):
        for key in range(len(l1)):
            if l1[key] != l2[key]:
                flag = 0
                break
    else:
        flag = 0

    if flag == 1:
        print("Strings are equal")
    else:
        print("Strings are not equal")

s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
eq_strings(s1, s2)
