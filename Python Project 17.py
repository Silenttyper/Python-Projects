def add(q,w):
    return q+w

def subtraction(e,r):
    return e-r

def multiplication(y,u):
    return y*u

def division(z,x):
    if division==0:
        ZeroDivisionError
        print("Can not divide by zero entre a number higher than 0.")
    return z,x

print("add,subtract,multiplication,division")

userchoice=input("Choose the operator you want to use from the list above. ")

if userchoice=="add":
     num1=int(input("Enter a number ")) 
     num2=int(input("Enter a second number "))
     additionresult=num1 + num2
     print(additionresult)
elif userchoice=="subtraction":
    subnum1=int(input("Enter a number ")) 
    subnum2=int(input("Enter a second number "))
    subtractionresult=subnum1=subnum2
    print(subtractionresult)
elif userchoice=="multiplication":
    mulnum1=int(input("Enter a number ")) 
    mulnum2=int(input("Enter a second number "))
    multiplicationresult=mulnum1*mulnum2
    print(multiplicationresult)
elif userchoice=="division":
    divnum1=int(input("Enter a number ")) 
    divnum2=int(input("Enter a second number "))
    divisionresult=divnum1 / divnum2
    print(divisionresult)




