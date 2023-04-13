teksts = input("Ievadiet garu tekstu: ")
check_nav = "nav"
replace_nav = "ir"
check_slikts = "slikts"
replace_slikts = "labs"
 
if check_nav in teksts and check_slikts in teksts:
    check_nav_index = teksts.index(check_nav)+len(check_nav)
    check_slikts_index = teksts.index(check_slikts)
else:
    print("Tekstā nav viens vai abi meklētie vārdi")
    print(teksts)
    print("Programma beigusies")
    exit()	# early exit

between = (teksts[check_nav_index+1:check_slikts_index])
replaced_text = teksts.replace(check_nav, replace_nav)
replaced_text = replaced_text.replace(check_slikts, replace_slikts)
replaced_text = replaced_text.replace(between, "")
print(replaced_text)