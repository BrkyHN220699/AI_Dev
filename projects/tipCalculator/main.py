print("Welcome to the Tip Calculator Mini-App")

totalBill = input("What was the total bill? ")
print()

totalTip = input("How much tip would you like to give? ")
print()

totalPeople = input("How many people to split the bill? ")
print()
print()

payBeforeTip = (float(totalBill) / int(totalPeople))
payAfterTip = payBeforeTip + ((payBeforeTip * int(totalTip)) / 100)



#pay = (int(totalTip) + int(totalBill)) / int(totalPeople)
print("Each person should pay: " ,round(payAfterTip, 2))

#print(f"Each person should pay {pay}")