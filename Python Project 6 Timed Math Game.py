#Timed Math Quiz Game
import random
import keyboard
import time

MINNUMBER=3
MAXNUMBER=12
OPERATIONS=["+","-","*"]
TOTALQUESTIONS=10

def mathproblem():
    left=random.randint(MINNUMBER,MAXNUMBER)
    right=random.randint(MINNUMBER,MAXNUMBER)
    operator=random.choice(OPERATIONS)
    mathequation=str(left) + " " + operator + " " + str(right)
    answer=eval(mathequation)
    return mathequation,answer


def spacebar():
    print("Press space to start")
    while True:
        if keyboard.is_pressed("space"):
            break
        time.sleep(0.1)
spacebar()


wrong =0
start_time=time.time()

for y in range(TOTALQUESTIONS):
    mathequation,answer=mathproblem()
    user_answer=input("Questions " + str(y+1) + ": " + " " + mathequation + " = ")
    if user_answer==str(answer):
        continue
    else:
        wrong+=1
   

end_time=time.time()
total_time=round(end_time-start_time)
print(f"You finished the math quiz in {total_time} seconds.")


