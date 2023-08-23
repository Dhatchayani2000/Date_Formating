# Date_Formating

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

