def checkPwT1():
    pw1 = input("Enter your password: ")
    pw2 = input("Repeat your password: ")
    return pw1 == pw2

def checkSeatTypeT2():
    seatNumber = int(input("Enter your seat number: "))
    if seatNumber <= 36:
        if seatNumber % 2 == 0:
            return "Cabin upper seat"
        else:
            return "Cabin lower seat"
    else:
        if seatNumber % 2 == 0:
            return "Open upper seat"
        else:
            return "Open lower seat"

def checkLeapYearT3():
    year = int(input("Enter year number: "))
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return f"The year {year} is a leap year"
    return f"The year {year} is not a leap year"

def colorMergeT4():
    colors=('red','blue','yellow')
    c1=input("Enter the first primary color: ")
    c2=input("Enter a second primary color: ")
    if c1 in colors and c2 in colors:
        if c1 != c2:
            if (c1 in ('red','blue')) and (c2 in ('red','blue')):
                return('Merge result: violet')
            if (c1 in ('red','yellow')) and (c2 in ('red','yellow')):
                return('Merge result: orange')
            if (c1 in ('blue','yellow')) and (c2 in ('blue','yellow')):
                return('Merge result: green')
        else:
            return("Merge result: same colors")
    else:
        return("Merge result: N/A")

print(colorMergeT4())
                    
        


