"""experiment no.4
Bubble Sort
name Abhinav Nair
roll no 4"""
from datetime import datetime
print(datetime.now())
List = []
no = int(input("Enter the number of elements: "))
for i in range(no):
    e = int(input("Enter element {}: ".format(i + 1)))
    List.append(e)

print("Original list:", List)

for i in range(no - 1):
    for j in range(no - i - 1):
        if List[j] >= List[j + 1]:
            List[j], List[j + 1] = List[j + 1], List[j]

print("Sorted list:", List)
