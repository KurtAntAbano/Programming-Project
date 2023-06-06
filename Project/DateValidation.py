date = input("input a date")

count = ()


def days_month_check(temp, days, months):
    global count


    month_dictionary = {31: [1, 3, 5, 7, 8, 10, 12], 30: [4, 6, 9, 11], 2: 28}
    if temp == True:
        month_dictionary[2] = 29

    if months in month_dictionary[31]:
        if days <= 31:
            count = True
        else:
            count = False

    elif months in month_dictionary[30]:
        if days <= 30:
            count = True
        else:
            count = False

    elif months == 2:
        if days <= month_dictionary[2]:
            count = True
        else:
            count = False

    else:
        count = False

    return count


def leap_year(years, days, months):
    div100 = years % 100


    if div100 != 0:
        answer = div100 % 4
        if answer == 0:
            temp = True
        else:
            temp = False
        days_month_check(temp, days, months)

    else:
        answer = years % 400
        if answer == 0:
            temp = True
        else:
            temp = False
        days_month_check(temp, days, months)


def format(date):
    datelen = len(date)


    if datelen != 10:
        temp = False
    else:
        temp = True
    return temp


def split(date):
    days = int(date[0:2])


    months = int(date[3:5])
    years = int(date[6:10])
    leap_year(years, days, months)


def main(date):
    x = format(date)


    while x == False:
        print("INVALID!")
        date = input("input a date")
        x = format(date)

    if x == True:
        split(date)
        if count == True:
            print("THIS DATE IS VALID!")
        elif count == False:
            print("THIS DATE IS INVALID!")
            date = input("input a date")
            main(date)

main(date)