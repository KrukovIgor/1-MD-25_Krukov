import random

def concatN():
    n = int(input("Enter the quantity of words: "))
    res = ""
    print("Enter the words: ")
    for i in range(n):
        buf = input()
        res += buf + " "
    return res
 
def concatInf():
    print("Enter the words: ")
    res = ""
    buf = input()
    while buf != "stop":
        res += buf + " " 
        buf = input()
    return res
    
def isRareWord():
    w = input("Enter the word: ")
    for i in w:
        if i in ['z', 'q', 'x']:
            return("It's a rare word")
    return("It's not a rare word")

def mathGame():
    lifeCounter = 3
    score = 0
    while lifeCounter != 0:
        a = random.randint(0, 999)
        b = random.randint(0, 999)
        print(f"{a} + {b} = ")
        buf = int(input("Your answer: "))
        if buf == (a + b):
            print("Correct!")
            score += 1
        else:
            lifeCounter -= 1
            print(f"Wrong answer! Lives left: {lifeCounter}")
    print("Game over")
    return(f"Score: {score}")
    
print(mathGame())