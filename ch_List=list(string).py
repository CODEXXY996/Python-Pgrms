ch_List=list(string)
count=0
for ch in ch_List:
  for ch2 in ch_List:
    if(ch==ch2):
      count+=1
  chardict[ch]=count
  count=0
print(chardict)

