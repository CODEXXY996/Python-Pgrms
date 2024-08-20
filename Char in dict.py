"""experiment no.2c





Character
name Abhinav Nair
roll no 4"""
from datetime import datetime
print(datetime.now())
chardict={}
string=input("enter the string ")
ch_list=list(string)
count=0
for ch in ch_list:
    for ch2 in ch_list:
        if(ch==ch2):
            count+=1
    chardict[ch]=count
    count=0
print(chardict)
