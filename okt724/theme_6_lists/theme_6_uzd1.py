# 1.a Vidējā vērtība
# Uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float).
# Programma pēc katra ievada rāda visu ievadīto skaitļu vidējo vērtību.
# PS. 1a var iztikt bez lists
# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus
# PS Iziešana no programmas ir ievadot "q"
# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.
moving_avg = 0.0 #mainīgais vidējais
cnt = 0 #skaitītājs

num_list = []
avg = 0.0
while True:
    input_str = input("Ievadiet skaitli vai nospiediet Q/quit, lai izietu ")
    if input_str.lower().startswith('q'): # very liberal check any string starting with q or Q
        break
    try:
        number = float(input_str)
        num_list.append(number)
    except ValueError as ex:
        continue # go back to input
 
    moving_avg += number
    cnt += 1
    avg = moving_avg/cnt
    also_avg = sum(num_list)/len(num_list)
    # sum works if all list elements are numbers (int, float)
    print(f"Ievadīto skaitļu vidējā vērtība {avg}")
    print(f"Arī ar sum funkciju {also_avg}")
print("Beigas")
#1b papildināts ar num_list
print(f'1b visi ievaditie skaitli: {num_list} un vidējā vērtība {avg}')

# let's show min and max values before sorting
print(f'Minimums ir {min(num_list)} un maksimums ir {max(num_list)}')
# we can do that before sorting
# finding min and max would be faster than sorting something big

# of course if he had sorted the list he could have done it in one line
# min would be num_list[0] and max would be num_list[-1]

num_list.sort()
print(f'1c TOP3 ievadītie skaitļi ir: {num_list[-3:][::-1]} un BOTTOM3:{num_list[:3]}, vidējā vērtība visiem skaitļiem {avg} ')

