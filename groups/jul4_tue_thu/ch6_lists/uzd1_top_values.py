# 1. Vidējā vērtība
# top = 3
# bottom = 3
# all_values = []
# while True:
#     usr_inpt = input('Ievadi skaitli: ')
 
#     if usr_inpt.lower() == 'q':
#         break
    
#     try:
#         usr_inpt = float(usr_inpt)
#         all_values.append(usr_inpt)
#         all_values.sort() # in place sorting
#         print(f'Ievadītie skaitļi: {all_values}')
#         print(f'top {top}: {all_values[:top]}, bottom {bottom}: {sorted(all_values, reverse=True)[:bottom]}')
#         print(f'Ievadīto skaitļu vid.vērtība: {round(sum(all_values)/len(all_values),4)}')
#     except ValueError:
#         print('Ievadītajai vērtībai ir jābūt skaitlim')

# # let's put the code into a function
# def top_values(values, top=3, bottom=3):
#     # sort the values
#     values.sort()
#     # return top and bottom values
#     return values[:top], sorted(values, reverse=True)[:bottom]

def my_avg(values):
    return round(sum(values)/len(values),4)
# there is also a built-in function for this
# import statistics
# statistics.mean(values)

# now let's create a big wrapper function for whole code
def show_values(top=3, bottom=3):
    all_values = []
    while True:
        usr_inpt = input('Ievadi skaitli: ')
    
        if usr_inpt.lower() == 'q':
            break
        
        try:
            usr_inpt = float(usr_inpt)
            all_values.append(usr_inpt)
            all_values.sort() # in place sorting
            print(f'Ievadītie skaitļi: {all_values}')
            print(f'top {top}: {all_values[:top]}, bottom {bottom}: {sorted(all_values, reverse=True)[:bottom]}')
            print(f'Ievadīto skaitļu vid.vērtība: {my_avg(all_values)}')
        except ValueError:
            print('Ievadītajai vērtībai ir jābūt skaitlim')

# call it
show_values()
# TODO deconstruct the code into more functions