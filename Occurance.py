def freq_str(s):
    l=sorted(list(s))
    g={}
    count=1
    for i in l:
        for i in g:
            g[i]+=1
        else:
            g[i]=1
        print(g)
l=[]
n=int(input("enter limit"))
for i in range(n):
      g=input("enter the string")
      l.append(g)
for i  in range(n):
      print("the frequency of",l[i])
      freq_str(l[i])
            
      
