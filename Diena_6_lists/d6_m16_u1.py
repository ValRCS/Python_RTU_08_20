## 1.uzdevums
# numberList = []
# print("Ievadam q(Q) lai izietu. ")
# while True: 
#     userInput = input("Ievadiet skaitli: ")
    
#     if userInput.lower().startswith("q"):
#         break
    
#     try:
#         number = float(userInput)
#         numberList.append(number)
#     except ValueError:
#         print("Tas nav skaitlis!")
#         continue
    
#     sortedList = sorted(numberList)
 
#     print("TOP3:", sortedList[::-1][:3] )
#     print("BOTTOM3 :", sortedList[:3])
#     print("Vidēja vērtība:", round(sum(numberList) / len(numberList), 2))

import statistics
 
my_list = []
while True:
    user_input = (input('Ievadiet skaitli'))
    if user_input.lower().startswith('q'):
        print('Quiting')
        break
    try:
        num = float(user_input)
    except ValueError:
        print('Not a number. Please enter number')
        continue
    my_list.append(float(user_input))
    my_list.sort(reverse=True) # IN PLACE SORT DESCENDING
    # my_list.sort() # ascending
    print(my_list[:3])
    print(my_list[-3:][::-1])
    print(statistics.mean(my_list))