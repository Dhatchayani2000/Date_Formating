import datetime
def givendate(DateFormat):
   date=datetime.datetime.strptime(DateFormat, "%Y/%m/%d")
   resultdate=date.strftime("%A,%Y %b %d")
   return resultdate

DateFormat=input("Enter The Date :")
print(givendate(DateFormat))
