def task1(val):
    if val % 5 == 0:
        return True
    else:
        return False
    
def task2(val):
    try:
        return 300 / val
    except ZeroDivisionError:
        print("Division by is 0!")
        
def task3(date):
    d = int(date[:2])
    m = int(date[3:5])
    y = int(date[8:10])
    if d * m == y:
        return True
    else:
        return False
    
def task4(num):
    c1 = 0
    c2 = 0
    i = 0
    for i in range(len(num)):
        if i < len(num)//2:
            c1 += int(num[i])
        else:
            c2 += int(num[i])
    if c1 == c2:
        return True
    else:
        return False
        
def taskSelector():
    taskN = int(input("Choose the task: "))
    if taskN == 1:
        n = int(input("Enter the number: "))
        print(task1(n))
    elif taskN == 2:
        try:
            n = int(input("Enter the number: "))
            print(task2(n))
        except ValueError:
            print("Not a number")
    elif taskN == 3:
        date = input("Input date in dd.mm.yyyy format: ")
        print(task3(date))
    elif taskN == 4:
        n = input("Input the number: ")
        print(task4(n))
    else:
        print("Unidentified command")
        
taskSelector()