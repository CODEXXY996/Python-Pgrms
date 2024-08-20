"""experiment no.4
linear search
name Abhinav Nair
roll no 4"""
from datetime import datetime
print(datetime.now())
from datetime import datetime

print(datetime.now())

def search(x, List):
    found = False
    for e in List:
        if e == x:
            found = True
            return found

no = int(input("Enter the number of elements: "))
List = []
for i in range(no):
    e = int(input("Enter the element {}:".format(i+1)))
    List.append(e)

x = int(input("Enter the element to search: "))
found = search(x, List)
if found:
    print("Element found")
else:
    print("Element not found")
