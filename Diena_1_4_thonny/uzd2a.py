exp=int(input("How many years have you worked for this company?"))
 
if exp <=2:
    input("Sorry, You will not be awarded a Christmas bonus!")
else:
    sal=input("How much euros is your salary?")
    bonus=round(float(sal) * 0.15 * (exp-2),2)
    print(f"Your Christmas bonus will be {bonus} euros!")