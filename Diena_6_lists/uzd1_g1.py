# Māras risinājums
total = 0
saraksts2 = []
n = 0
while True:
    skaitlis = input("ievadi skaitli vai q lai beigtu")
    if skaitlis == "q":
        break
    skaitlis = float(skaitlis)  # TODO check for correct numeric types
    total += skaitlis
    n += 1
    saraksts2.append(skaitlis)
    saraksts2 = sorted(saraksts2, reverse=True)
    print(
        f"Top3 ir {saraksts2[:3]} \n Bottom3 ir {saraksts2[-3:]} \n ievadīto skaitu vid.vērtība ir {total/n}")
