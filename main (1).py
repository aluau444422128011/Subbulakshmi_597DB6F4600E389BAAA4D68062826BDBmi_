# how to check leap year
year=int(input("enter the year:"))

if(year%400==0) and (year%100==0):
  print(year,"is leap year " )

if(year%4==0) and (year%100!=0):
  print (year,"is leap year ")

else:
  print(year,"is not leap year")