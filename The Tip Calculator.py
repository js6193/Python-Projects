print('Welcome To The Tip Calculator')
amount = float(input("What was the total bill?"))
tip = int(input("What percentage tip would you like to give ? 10, 12, 15 "))
tip_perc = tip/100
split = int(input("How many person to split the bill ?"))
tip_amt = amount*tip_perc
total_amt = amount+tip_amt
per_pers_amt = total_amt/split
round_of_per_pers_amt= round(per_pers_amt,2)
print(f"Each person should pay {round_of_per_pers_amt}")