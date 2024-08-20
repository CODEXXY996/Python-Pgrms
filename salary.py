hourlywage=int(input("enter the hourly wage"  ))
totalhours=int(input("enter the total hours worked"  ))
overtime=int(input("enter the over time worked"  ))
overtimepay=1.5*hourlywage*overtime
print("over time payment is :" ,overtimepay)
regularpay=hourlywage*totalhours
weeklypay=regularpay+overtime
monthlypay=4*weeklypay
print("monthly payment ;",monthlypay)