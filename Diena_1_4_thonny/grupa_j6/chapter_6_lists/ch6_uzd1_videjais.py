#1.a uzd
l = []
while True:
    inp = input("Lūdzu ievadiet skaitli vai (Q)uit beigšanai: ")
    if inp.lower().startswith('q'): #so we can quit with Q or q or Quit or quit
        print("All done")
        break
    try:
        l.append(float(inp))
    except ValueError:
        print("Nepareiza ievade, nepieciešams skaitlis")
        continue
    vid = sum(l)/len(l)
    print(f"Skaitļu vidējā vērtība ir {vid:.2f}") # 2 decimal places
    l.sort() # sort the list IN PLACE ascending - modifies the list
    top = l[-3:][::-1] # reverse because we want descending for top 3
    bottom = l[:3]
    print(f"Skaitļu vidējā vērtība ir {vid:.2f}, top 3 {top}, apakšējie 3 {bottom}")
 