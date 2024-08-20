chardict={}
string=input("enter the string  ")
ch_list=list(string)
c=0
for ch in ch_list:
    for ch2 in ch_list:
        if(ch==ch2):
            c+=1
        chardict[ch]=c
        c=0
    print(chardict)

