########################################################################################################################
#  Name: Kurt
#  purpose of module: create functions for all validation checks I need
#  bugs or notes: added isStringCHeck and isNumericCheck, next time use regex for data format and phone number
#  date:  04/05/23
########################################################################################################################


def is_valid_email(email):
    from validate_email import validate_email

    isExists = validate_email(email, verify=True)
    if isExists:
        return True
    else:
        return False



def isStringCheck(text):  # checks if the text is a string
    is_string = isinstance(text, str)
    if is_string:
        return True
    else:
        return False


def isNumericCheck(text):  # checks if the text is an integer
    is_integer = isinstance(text, int)
    if is_integer:
        return True
    else:
        return False


def isValidLength(text, length, state):  # function checks whether the string is the appropriate length
    if state == 1:
        if len(text) == length:
            return True
        else:
            return False

    elif state == 2:
        if len(text) >= length:
            return True
        else:
            return False

    elif state == 3:
        if len(text) >= length:
            return True
        else:
            return False



def presenceCheck(text):  # function checks if the text is empty
    if len(text) == 0:
        return False
    else:
        return True


def rangeCheck(text, lower_limit, upper_limit):  # function will take the upper and lower limit and check whether text
    #  is within that range
    if lower_limit < len(text) < upper_limit:
        return True
    else:
        return False


def dateFormatCheck(text):  # checks if a string is in the correct date format
    if len(text) == 10:
        if text[2] == "/" and text[5] == "/":
            return True
        else:
            return False
    else:
        return False
    #  incorporate the date validation file into this function to check whether the dat can actually exist
    #  create a function called, 'isValidDate()'


if __name__ == "__main__":
    # print(dateFormatCheck("04/12/2005"))
    # print(rangeCheck("Hello World", 1, 3))
    # print(presenceCheck(""))
    print(isValidLength("Hello World", 11))
    print(isStringCheck(6))
