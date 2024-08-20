data = []
name = input("Enter the name: ")
dob = input("Enter date of birth (dd/mm/yy): ")
data.append(name)
date = dob.split("/")
data.extend(date)
datadict = {}
datadict['name'] = data[0]
datadict['day'] = data[1]
datadict['month'] = data[2]
datadict['year'] = data[3]
print("The birthday of {} is {}-{}-{}".format(datadict['name'], datadict['day'], datadict['month'], datadict['year']))
