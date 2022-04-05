#1. Uzdevums
import datetime # par importiem runāsim atsevišķi
current_year = datetime.datetime.now().year
target_age = 1_000
your_age = int(input("Kāds ir Jūsu vecums?"))
age_delta = target_age - your_age
print(f"Jums būs {target_age} gadi pēc {age_delta} gadiem")
target_year = age_delta + current_year
print(f"Jūs būsiet {target_age} gadus vecs {target_year} gadā")