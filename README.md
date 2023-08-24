# UserDesired_Date_Formating

## Format Codes or Sepcification Can be used in this program:

%a Weekday as Sun, Mon

%A Weekday as full name as Sunday, Monday 

%w Weekday as decimal no as 0,1,2...

%d Day of month as 01,02

%b Months as Jan, Feb

%B Months as January, February

%m Months as 01,02

%y Year without century as 11,12,13

%Y Year with century 2011,2012

%H 24 Hours clock from 00 to 23

%I 12 Hours clock from 01 to 12

%p AM, PM

%M Minutes from 00 to 59

%S Seconds from 00 to 59

%f Microseconds 6 decimal numbers


## Introduction
The script uses the datetime module to handle date and time-related operations.

This script also defines a function formatting_date that takes a date from userdefined format as input and converts it into the User Desired format.

## Usage
Enter a date in any format as user needs when prompted.

The script will output the converted date in the User Desired format

You will be prompted to enter the following inputs:

UsergivenDate: The date you want to format (e.g., "2023-08-24").

UsergivenDateFormat: The format of the input date you provided (e.g., "%Y-%m-%d").

DesiredFormatofUser: The format you want the output date to be in (e.g., "%d-%m-%Y").

## Function Signature
def formatting_date(UsergivenDate, UsergivenDateFormat, DesiredFormatofUser):
    """
    Convert a given date from one format to another format.

    Args:
        UsergivenDate (str): The input date provided by the user.
        UsergivenDateFormat (str): The format of the input date.
        DesiredFormatofUser (str): The desired format for the output date.

    Returns:
        str: The input date converted to the desired format.
    """


  ## Example:
  Suppose you want to format the date "2023-08-24" from the format "YYYY-MM-DD" to "DD/MM/YYYY". Here's how you would use the script: 
  
  Enter The Date: 2023-08-24
  
  Enter The Format: %Y-%m-%d
  
  Enter The Desired Format: %d/%m/%Y
  
  Formatted Date: 24/08/2023


