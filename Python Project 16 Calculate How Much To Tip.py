#Calculating Tip
would_you_like_to_tip=input("Would you like to tip? Y/N ")
if would_you_like_to_tip=="Y":
    dinner_bill=int(input("Enter you dinner bill "))
    tip_percent=(int(input("Enter a percent you want to tip ")))
    tip_amount=dinner_bill*(tip_percent /100)
    print(tip_amount)
