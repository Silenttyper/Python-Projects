print("Welcome to my computer quiz! ")

playing = input("Do you want to play? ")
print(playing)
if playing !="yes":
    quit()
print("Okay Lets Play")
score=0

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print("Correct! ")
    score+=1
else:
    print("Incorreect! ")

answer=input("What is the full form of RAM? ")
if answer=="Random Access Memory":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does GPU stand for? ")
if answer=="Graphics Processing Unit":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does the acronym SSD stand for? ")
if answer=="Solid State Drive":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does BIOS stand for? ")
if answer=="Basic Input/Output System":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does USB stand for? ")
if answer=="Universal Serial Bus":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What is the full form of the acronym HTTP? ")
if answer=="Hypertext Transfer Protocal":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does LAN stand for? ")
if answer=="Local Area Network":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What is the full form of DNS? ")
if answer=="Domain Name System":
    print("Correct!")
    score+=1
else:
    print("Incorrect!")

answer=input("What does HTML stand for? ")
if answer=="Hyper Text Markup Language":
    print("Correct!")
    score+=1
else:
    print("incorrect!")
print("Your score is "+ str((score/10)*100 )+"%")
