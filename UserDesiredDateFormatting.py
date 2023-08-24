from datetime import datetime

def formatting_date(UsergivenDate,UsergivenDateFormat,DesiredFormatofUser):
  Date=datetime.strptime(UsergivenDate,UsergivenDateFormat)
  return Date.strftime(DesiredFormatofUser)

UsergivenDate=input("Enter The Date :")
UsergivenDateFormat=input("Enter The Format :")
DesiredFormatofUser=input("Enter The Desired Format :")

output=formatting_date(UsergivenDate,UsergivenDateFormat,DesiredFormatofUser)
print(output)
