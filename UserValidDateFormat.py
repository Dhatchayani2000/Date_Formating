from datetime import datetime
import re
class InvalidDateFormatError(Exception):
    def __init__(self, message):
        super().__init__(message)

ALLOWED_FORMAT_CODES = {
    "%Y", "%y", "%m", "%d", "%H", "%I", "%M", "%S",
    "%p", "%b", "%B", "%a", "%A", "%j", "%w", "%U",
    "%W", "%Z" ,"%f", "%z" ,"%c", "%C", "%X", "%x"
}

def validate_format(format_string):
    customdelimiters = [' ', ':', '-', '/', ',']
    parts = filter(None, re.split('|'.join(map(re.escape, customdelimiters)), format_string))
    
    for code in parts:
        if code not in ALLOWED_FORMAT_CODES:
            return False
    return True


def formatting_date(UsergivenDate, UsergivenDateFormat, DesiredFormatofUser):
    if not validate_format(DesiredFormatofUser):
        raise InvalidDateFormatError("Error: Desired format contains invalid format codes")
    
    if UsergivenDate.isdigit():
        raise InvalidDateFormatError("Error: Input contains only numbers")

    try:
        Date = datetime.strptime(UsergivenDate, UsergivenDateFormat)
        formatted_date = Date.strftime(DesiredFormatofUser)
        return formatted_date
    except ValueError as e:
        raise InvalidDateFormatError(f"Error: {e}")

UsergivenDate = input("Enter The Date (e.g., 2023-08-25 08:34:56): ")
UsergivenDateFormat = input("Enter The Format (e.g., %Y-%m-%d %H:%M:%S): ")
DesiredFormatofUser = input("Enter The Desired Format (e.g., %B %d, %Y %c): ")

try:
    output = formatting_date(UsergivenDate, UsergivenDateFormat, DesiredFormatofUser)
    print("Formatted Date:", output)
except InvalidDateFormatError as e:
    print(e)


