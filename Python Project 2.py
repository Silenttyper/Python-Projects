#Computer quiz game like the first project but this is multiple choice questions
print("Welcome To Our Quiz Game")
user_response=input("Would you like to start type Y/N ")
if user_response=="Y":
    print("Great let's get started!")
else:
    quit()
score=0
print("Question 1")
answer=input("What is the main point of a for loop?\n(Type A,B,C,D to answer)\n A) To iterate over a sequence \n B) To define a function \n C) To perform arithmetic operations \n D) To declare variables ")
if answer=="A":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is A ")

print("Question 2")
answer=input("What is the difference between == and = in Python?\n Choose A,B,C,D to answer \n A) Both are used for comparison \n B) == is used for assignment, = is used for comparison \n C) == is used for comparison, = is used for assignment \n D) Both are used for assignment ")
if answer=="C":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is C.")

print("Question 3")
answer=input("What does the funciton .append() do in a list in Python? \n Choose A,B,C,D \n A) Removes an element from the list \n B) Adds an element to the end of the list \n C) Sorts the list in ascending order \n D) Reverses the order of elements in the list ")
if answer=="B":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is B. ")

print("Question 4")
answer=input("How do you comment out multiple lines of code in Python? \n Choose A,B,C,D \n A) Using # symbol before each line \n B) Using // symbol before each line \n C)Using triple quotes \n D) Using /* */ around the lines ")
if answer=="C":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is C.")

print("Question 5")
answer=input("What does the .len( do in Python \n Chose A,B,C,D \n A) Returns the length of a string \n B) Returns the length of a list \n C) Returns the length of a tuple \n D) All of the above) ")
if answer=="D":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is D.")

print("Question 6")
answer=input("What does the range function return in Python? \n Choose A,B,C,D \n A) A list of integers \n B) A string \n C) A tuple \n D) A sequence of numbers ")
if answer=="D":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is D. ")

print("Question 7")
answer=input("What does the .pop() do in Python?\n Choose A,B,C,D \n A) Adds an element to the end of the list \n B) Removes and returns the last element from the list \n C) Removes and returns the first element from the list \n D) Removes all elements from the list ")
if answer=="B":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is B")

print("Question 8")
answer=input("What does the strip() funciton do in Python? \n Choose A,B,C,D \n A) Removes leading and trailing whitespace characters \n B) Converts the string to uppercase \n C) Replaces characters in the string \n D) Splits the string into a list of substrings ")
if answer=="A":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is A.")

print("Question 9")
answer=input("What does the .sort() function do in Pyhton list? \n Choose A,B,C,D \n A) Sorts the list in descending order \n B) Sorts the list randomly \n C) Sorts the list in ascending order \n D) Returns a sorted copy of the list ")
if answer=="C":
    print("Correct!")
    score+=1
else:
    print("Incorrect! The correct answer is C. ")


print("Question 10")
answer=input("What is a dictionary in Python? \n Choose A,B,C,D \n A) An ordered collection of items \n B) A collection of elements accessed by index \n C) An unordered collection of key-value pairs \n D) A sequence of immutable elements")
if answer=="C":
    print("C")
else:
    print("Incorrect! The correct answer is C. ")

print("Your score is" + int((score/10)* 100)+ "%")
