# 1.uzdevums no 3.dienas
temp_body = float(input("Kāda ir Jūsu temperatūra? "))
if temp_body < 35:
    print("Jums laikam ir pārāk auksti, vajadzētu pasildīties 🥶")
elif 35 <= temp_body <= 37:
    print("Jums viss ir kārtībā 😊")
else:
    print("Jums varētu būt drudzis 🤒")