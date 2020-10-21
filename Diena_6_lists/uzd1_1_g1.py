#### 1. UZDEVUMS ######################
i=0
avg=0
total=0
num_list = []
while True:
    num=input("Ievadiet skaitli vai 'q', lai izietu:")
    if num == 'q':
        break
    float_num = float(num)
    i+= 1
    avg = (total + float_num) / i
    total += float_num
    print(f"Vidējais: {avg}")
    num_list.append(float_num)
    sort_list = sorted(num_list, reverse=True)
    print(f"Ievadītie skaitļi: Top3 {sort_list[:3]}, Bottom3 {sort_list[-3:]}")

# digits = []
# digits = input("enter multiple digits, separate by space: or q to exit ")
# if digits.lower().startswith("q"):
#     exit()
# float_digits = [float(item) for item in digits.split()] # list comprehension
 
# count = len(float_digits)
# total = sum(float_digits)
# print(f"Average is {total/count} and entered digits are {digits}")
 
# sorted_1 = sorted(float_digits)
# print(f"TOP3 = {sorted(sorted_1[-3:],reverse=True)} and BOOTOM3 = {sorted_1[:3]} and average is {total/count}")

# # sk = 0
# # beigt = False
# # summa = 0
# # while not beigt:
# #     skaitlis = input("Ievadiet skaitli (ievadiet q, lai beigtu): ")
# #     if skaitlis.lower().startswith("q"):
# #         break
# #     skaitlis = float(skaitlis)
# #     summa += skaitlis
# #     sk += 1
# #     print(f"Ievadīto skaitļu vidējā vērtība ir {summa / sk}")

# all_numbers=[]
# while True:
#     numbers=input("Ievadiet skaitli vai 'q', lai pabeigt - ")
#     if numbers=="q":
#         break
#     else:
#         all_numbers.append(float(numbers))
#         n=len(all_numbers)
#         summa=sum(all_numbers)
#         continue
# print(f"Saraksts: {all_numbers}, kopēja summa: {summa}, vidēja vērtība: {summa/n}")
# all_asc=sorted(all_numbers)
# all_desc=sorted(all_numbers)
# print(f"TOP 3:{all_desc[-3:]} un vidēja vērtība:{round(sum(all_desc[-3:])/3)} & BOTTOM 3:{all_asc[:3]} un vidēja vērtība: {round(sum(all_asc[:3])/3, 2)}")