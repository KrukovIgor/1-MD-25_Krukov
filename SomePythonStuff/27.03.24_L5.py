import random

def task1():
    vals = []
    n = int(input("Enter your digit (0,9): "))
    for i in range(5):
        vals.append(random.randint(0,9))
        print(vals[i], end = " ")
    print (f"\n{n}")
    if n in vals:
        print("Correct!")
    else:
        print("Wrong!")
    
def task2():
    vals = []
    reps = []
    f = False
    for i in range(100):
        vals.append(random.randint(0,9))
    for i in range(100):
        if vals[i] not in reps:
            for j in range(100):
                if vals[i] == vals[j]:
                    reps.append(vals[j])
                    break
    for i in range(len(reps)):
        print(reps[i], end = " ")
        
def task3():
    days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
    n = int(input("Weekend duration: "))
    print("Your weekend:", end = " ")
    for i in range(n):
        print(days[-(i+1)], end = " ")
    print("\nWorking days:", end = " ")
    for i in range(len(days)-n):
        print(days[i], end = " ")
        
def task4():
    group1 = []
    group2 = []
    
    

task3()