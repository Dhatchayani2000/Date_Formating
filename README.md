## Allowed Format Codes
The script supports the following datetime format codes:

%Y: Year with century as a decimal number (e.g., 2023)

%y: Year without century as a zero-padded decimal number (e.g., 23 for 2023)

%m: Month as a zero-padded decimal number (e.g., 02 for February)

%d: Day of the month as a zero-padded decimal number (e.g., 09)

%H: Hour (24-hour clock) as a zero-padded decimal number (e.g., 14 for 2:00 PM)

%I: Hour (12-hour clock) as a zero-padded decimal number (e.g., 02 for 2:00 PM)

%M: Minute as a zero-padded decimal number

%S: Second as a zero-padded decimal number

%p: AM or PM designation for time (e.g., AM or PM)

%b: Abbreviated month name (e.g., Jan)

%B: Full month name (e.g., January)

%a: Abbreviated day of the week (e.g., Mon)

%A: Full day of the week (e.g., Monday)

%j: Day of the year as a zero-padded decimal number (e.g., 365)

%w: Weekday as a decimal number (0 = Sunday, 6 = Saturday)

%U: Week number of the year (Sunday as the first day of the week)

%W: Week number of the year (Monday as the first day of the week)

%Z: Time zone name

## Introduction
The script uses the datetime module to handle date and time-related operations. 

It provides input validation for the desired date format and handles custom exceptions for better error handling.


## Usage
Enter a date in any format as user needs when prompted.

The script will output the converted date in the User Desired format

## Input Instructions
Enter the date you want to format (e.g., 2023-08-25 08:34:56).

Enter the current format of the date (e.g., %Y-%m-%d %H:%M:%S).

Enter the desired format for the output (e.g., %B %d, %Y %c).

The script will then attempt to format the date according to your specifications.

If the format codes provided are not allowed or if the input date contains only numbers, appropriate error messages will be displayed.

## Function Signature
### `validate_format(format_string)`

- **Input:** `format_string` (str) - The desired output date format.
- **Output:** `True` if the format is valid, `False` otherwise.

This function checks if the provided `format_string` contains only valid datetime format codes. It uses predefined `ALLOWED_FORMAT_CODES` and checks each part against it.

### `formatting_date(UsergivenDate, UsergivenDateFormat, DesiredFormatofUser)`

  **Input:**
  - `UsergivenDate` (str) - The original date.
   
  - `UsergivenDateFormat` (str) - The format of the original date.
   
  - `DesiredFormatofUser` (str) - The desired output date format.
    
  **Output:** Formatted date (str) if successful, raises `InvalidDateFormatError` otherwise.
  
  This function takes user inputs, validates the desired output format using `validate_format`, and then uses `datetime` operations to parse and format the date.

  It handles errors by raising custom `InvalidDateFormatError` exceptions.

### `InvalidDateFormatError(Exception)`

  This is a custom exception class that inherits from the base `Exception` class.

  It's used to handle specific errors related to invalid date formats. It can be raised with custom error messages.


  ## Example:
  Suppose you want to format the date "2023/08/24 12:34:56" from the format "YYYY-MM-DD HH:MM:SS" to "DD/MM/YYYY SS:MM:HH(AM/PM) ". Here's how you would use the script: 
  
  Enter The Date (e.g., 2023-08-25 08:34:56): 2023/8/31-12:34:56 
  
  Enter The Format (e.g., %Y-%m-%d %H:%M:%S): %Y/%m/%d-%H:%M:%S 
  
  Enter The Desired Format (e.g., %B %d, %Y %c): %A,%d-%m-%Y %H:%M:%S %p 
  
  Formatted Date: Thursday,31-08-2023 12:34:56 PM


