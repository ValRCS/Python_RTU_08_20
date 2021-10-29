from statistics import mean
# def get_min_avg_max(numbers) -> tuple:
#     """
#     Funkcija, kas atgriež min, vidējo vērtību un maksimālo vērtību
#     no skaitļu saraksta.
#     """
#     return (min(numbers), sum(numbers) / len(numbers), max(numbers))

def get_min_avg_max(numbers) -> tuple:
    """
    Funkcija, kas atgriež min, vidējo vērtību un maksimālo vērtību
    no skaitļu saraksta.
    """
    return min(numbers), mean(numbers), max(numbers)

print(get_min_avg_max([1, 2, 3, 4, 5]))
print(get_min_avg_max([3,9,1,2]))

# # Uzd 1b #
def get_min_med_max(b_sequence): # Function
    b_sequence = tuple(sorted(b_sequence)) #variable as tuple & sort
    min_res = b_sequence[0]  # call and write a min value of sorted list
    max_res = b_sequence[-1] # call and write amax value of sorted list
    len_res = int(len(b_sequence)) #call a count of values in list convert lenth to integer
    if len_res % 2 == 0: #check for a/2
        if type(b_sequence[0]) != str: #check for var type should not be a string
            med_res= (b_sequence[int(len_res/2) - 1] + b_sequence[int(len_res/2)])/2 # medium result with converted count of 
            # print(my_med)
        else:
            med_res= (b_sequence[int(len_res/2)-1] + b_sequence[int(len_res/2)])
    else:
        med_res= b_sequence[int(len_res/2)]
    return min_res, med_res, max_res

print(get_min_med_max([1,5,8,4,3]))  
print(get_min_med_max([2,2,9,9,4,3]))
print(get_min_med_max("baaac"))
print(get_min_med_max("faaacb"))