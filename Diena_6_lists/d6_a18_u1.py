# 1.a Vidējā vērtība
# us_list = []
# game = True
# while game:
#     ch=input("Ievadiet skaitli ")
#     if ch == "q": 
#         game = False
#     else:
#         us_list.append(int(ch))
#         #print(us_list)
#         print ("Top 3:")
#         print(sorted(us_list)[-3:])
#         print ("Bottom 3:")
#         print(sorted(us_list)[:3])
#         avg = round(sum(us_list)/len(us_list), 2)   
#         print(avg)

my_list = []
while True:
    num = input("Ievadiet skaitli (vai 'q' lai izietu): ")
    if num == "q" or num == "Q":
        break 
    try:    
        num = float(num)
    except ValueError:
        print("Nepareiza vērtība")
        continue
    my_list.append(num)
    avg_my_list = sum(my_list)/len(my_list)
    my_list.sort(reverse=True)
    if len(my_list)<=6:
        print(f"Ievadītie skaitļi --> {my_list}")   
    else:
        min_max_list = my_list[:3] + my_list[-3:]
        print(f"Ievadīto skaitļu TOP3 un BOTTOM3 --> {min_max_list}")
    print(f"Visu ievadīto skaitļu vidējā vērtība --> {round(avg_my_list,4)}")