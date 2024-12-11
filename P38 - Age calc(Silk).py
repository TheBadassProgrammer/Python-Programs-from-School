#Age Calculator

day = int(input("Enter today's day: "))
month = int(input("Enter ongoing month: "))
year =  int(input("Enter ongoing year: "))

bday = int(input("Enter day of your DOB: "))
bmonth = int(input("Enter month of your DOB: "))
byear =  int(input("Enter year of your DOB: "))

if(day<bday):
   tday = (day+30)-bday
   month = month-1
else:
   tday = day-bday
   
if(month<bmonth):
   tmonth = (month+12)-bmonth
   year = year-1
else:
   tmonth = month-bmonth

tyear = year-byear

print("You are", tyear, "years", tmonth, "months", tday, "days old :)")
