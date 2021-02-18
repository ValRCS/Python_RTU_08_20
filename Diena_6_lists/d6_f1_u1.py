my_list = []
quit = "q"
while True:
    num = input("Please enter number (or q to quit): ")
    if num == quit:
        break
    else:
        my_list.append(float(num))
        my_list.sort()
        print(f"Top 3 numbers are {my_list[-1:-4:-1]} and Bottom 3 numbers are {my_list[0:3]}")

# saraksts=[]
 
# while True:
#     skaitlis = (input(f"ievadi float skaitli vai ievadi q lai izietu no loop "))
#     if skaitlis[0] == "q":
#         break
#     else:
#         saraksts.append(float(skaitlis))
#         print(f"Videja vertiba: {round(sum(saraksts) / len(saraksts), 2)}, Visi skaitļi: {saraksts}") # 1b uzdevumam
#         print(f"lielakie 3 skaitli: {list(reversed(sorted(saraksts)))[:3]}, mazakie 3 skaitli:{sorted(saraksts)[:3]} ")