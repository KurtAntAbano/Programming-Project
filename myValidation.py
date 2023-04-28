

def isValidLength(text, length, s):
    x = isinstance(text, str)
    if x:
        if s == "0":
            if len(text) == length:
                return True
            else:
                return False

        elif s == "1":
            if len(text) > length:
                return True
            else:
                return False

