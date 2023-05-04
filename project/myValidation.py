########################################################################################################
#  Name: Kurt
#  purpose of module:
#  bugs or notes:
#  date:
########################################################################################################




def isValidLength(text, length, s):
    x = isinstance(text, str)
    if x:
        match s:
            case "0":
                if len(text) == length:
                    return True
                else:
                    return False

            case "1":
                if len(text) > length:
                    return True
                else:
                    return False


def prescenceCheck(text):
    if text == " ":
        return False
    else:
        return True


def rangeCheck(text, lm, ul):
    if lm < len(text) < ul:
        return True
    else:
        return False


def formatCheck(text):
    if len(text) == 10:
        if text[2] == "/" and text[5] == "/":
            return True
        else:
            return False
    else:
        return False
