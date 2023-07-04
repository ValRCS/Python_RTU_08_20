import datetime # from standard library built into Python
target_age = 100 # maybe this number would come from outside
#ask name 
name = input("What is your name friend? ")
#ask age and cast to integer
age = int(input(f"How old are you, {name} ? "))
# to be more precise would be to ask how old they will be
# AFTER birthday this year

#calculate 
remaining_years = target_age - age
#calculate year
current_year = datetime.datetime.now().year
target_year_reached  = current_year + remaining_years
#print
# i can use triple quotes to make multiline stringes
print(f"""You will reach {target_age} in {remaining_years} years,
at {target_year_reached}.
That is impressive!""")
# otherwise I would have to use \n for newlines \t for tabs etc