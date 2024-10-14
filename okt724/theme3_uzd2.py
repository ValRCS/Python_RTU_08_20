# 2. uzdevums noprasiet lietotājam mēneša algas apjomu un nostrādāto gadu skaitu
MIN_YEARS = 2 # in longer program you would want to specify what MIN_YEARS refer to
BONUS_RATE = 0.15
monthly_salary = float(input("Please enter your monthly salary: "))
work_experience = float(input("How many years you have been employed? "))

if work_experience > MIN_YEARS:
#     eligible_years = int(
#         work_experience - MIN_YEARS
#     )  # during the first two years, we are not earning bonuses.
    eligible_years = work_experience - MIN_YEARS
    bonus = monthly_salary * eligible_years * BONUS_RATE
    print(f"You are eligible for a yearly bonus! Your bonus is {bonus:.2f}!")
else:
    print("Sorry, but you are not eligible for the bonus")

print("---------------")