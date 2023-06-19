total = 0
count = 0
number_list = []
 
while True:
    user_input = input("Ievadiet skaitli vai 'q', lai beigtu darbību: ")
    
    # if user_input.lower() == 'q':
    if user_input.lower().startswith('q'):  #we allow QUIT, quit, Quit, qUIT, etc.
        break
    
    try:
        number = float(user_input)
        number_list.append(number)
        total += number
        count += 1
        average = total / count
        print("Šībrīža vidējā vērtība: ", average)
        print("Visi ievadītie skaitĻi: ", number_list)
 
        if count >= 3:
            sorted_numbers = sorted(number_list) # so sorted returns a new list!
            # original list is not changed - sorted is OUT OF PLACE method
            # there is also sort method which is IN PLACE method
            # so it changes the list
            # number_list.sort() # this would sort the list in place - old list is lost

            top3_max_values = sorted_numbers[-3:]
            top3_min_values = sorted_numbers[:3]
            print("Trīs augstākās ievadītās vērtības:", top3_max_values)
            print("Trīs zemākās ievadītās vērtības:", top3_min_values)
 
    except ValueError:
        print("Lūdzu ievadiet derīgu skaitli.")
 
if count > 0:
    print("Beigu vidējā vērtība: ", average)
    sorted_numbers = sorted(number_list)
    top3_max_values = sorted_numbers[-3:]
    top3_min_values = sorted_numbers[:3]
    print("Trīs augstākās ievadītās vērtības:", top3_max_values)
    print("Trīs zemākās ievadītās vērtības:", top3_min_values)
 
else:
    print("Nav ievadīts neviens skaitlis.")