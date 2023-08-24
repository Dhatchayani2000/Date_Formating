# Date_Formating

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
This script defines a function givendate that takes a date in the format "YYYY/MM/DD" as input and converts it into the format "Day of the Week, Year Month Day".
The script uses the datetime module to handle date and time-related operations.

## Usage
Enter a date in the format "YYYY/MM/DD" when prompted.
The script will output the converted date in the format "Day of the Week, Year Month Day".

## Function Signature
import datetime

def givendate(DateFormat):
    """
    Convert a date from input format "YYYY/MM/DD" to "Day of the Week, Year Month Day" format.
    
    Parameters:
        DateFormat (str): The date in the format "YYYY/MM/DD".
        
    Returns:
        str: The converted date in the format "Day of the Week, Year Month Day".
    """
    date = datetime.datetime.strptime(DateFormat, "%Y/%m/%d")
    resultdate = date.strftime("%A, %Y %b %d")
    return resultdate

  ## Example:

Suppose you run the script and enter the date "2023/08/23" as input.
The script will convert this date into the format "Tuesday, 2023 Aug 23" and print the result.

