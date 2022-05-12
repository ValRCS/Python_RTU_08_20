# Ex 1
 
my_list = []
while True:
    user_input = input("Enter a number or Q if you want to Quit: ")
    if user_input.lower().startswith("q"):
        break
    try:
        num = float(user_input)
    except ValueError:
        print("Not a number!")
        continue
    my_list.append(num)
    print(my_list)
    average = round(sum(my_list)/len(my_list),2)
    print(f"Average value is: {average}")
   
# Showing only lowest and highest values in the list
 
sorted_list = sorted(my_list) # OUT OF PLACE OPERATION, original list is not changed
print(f"Lowest value is: {sorted_list[0]} and highest value is: {sorted_list[-1]}")
print("TOP 5 ascending", sorted_list[-5:])
print("BOTTOM 5", sorted_list[:5])