name=input("Enter your name ")
print("Welcome" + name + "to this adventure!")
answer="You are on a dirt road. It has come to an end  And you can go left or right."
if answer=="Letft":
    answer=input("You come to a river. You can walk around it or swimo across? Type walk to walk around it or type swim to swim across." )
    if answer=="swim":
        print("You swam across and was eaten by a aligator")
    elif answer=="walk":
        print("You walked for many miles, ranned out of water and you lost the game")
    else:
        print("Not a valid option. You lose!")
elif answer=="right":
    answer=input("You come to a bridge, it looks wobbly, do you want to cross it or head back?(Type cross or back) ")
    if answer=="back":
        print("You go back and lose!")
    elif answer=="cross":
        print("You crossed the bridge and eet a stranger. Do you talk to them (yes/no)?")
        if answer=="yes":
            print("You talked to the stranger and they gave you gold. You win!")
        elif answer=="no":
            print("You ignore the stranger and they feel offended. You lose!")
        else:
            print("Not a valid option. You lose!")
else:
    print("Not a valid option. You lose!")

print("Thank you for trying" + name)