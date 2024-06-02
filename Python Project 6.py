import random
import time

OPERATORS=["+","-","*"]
MIN_OPERATOR=3
MAX_OPERATOR=12
TOTAL_PROBLEMS=10
def generate_problem():
    left=random.randint(MIN_OPERATOR,MAX_OPERATOR)
    right=random.randint(MIN_OPERATOR,MAX_OPERATOR)
    operator=random.choice(OPERATORS)
    expr = str(left) + " "+ operator + " " + str(right)
    answer=eval(expr)
    return expr,answer

wrong=0 #This means they have zero questions wrong
print(input("Press (enter) to start"))
print("-----------------------")
start_time=time.time() #Counts in seconds since time start


for xyz in range(TOTAL_PROBLEMS):
    expr,answer= generate_problem()
    while True:
        guess=input("Problem #" + str(xyz+1) + ":" + expr + "= ")
        if guess==str(answer):
            break
        wrong==1 #This means if they get the question wrong python will add 1 to wrong answers every time
end_time=time.time() #You use time.time() to end the time count
total_time= round(end_time-start_time)
print("-----------------------")
print(f"Nice work. You finished in {total_time} seconds")