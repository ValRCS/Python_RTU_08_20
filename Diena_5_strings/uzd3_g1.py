fraze = input("Ievadiet savu tekstu: ")
ir_nav = fraze.find("nav")
ir_slikts = fraze.rfind("slikts")
#print(ir_nav, ir_slikts)
if ir_nav == -1 or ir_slikts == -1 or ir_nav > ir_slikts:
    print(fraze)
else: # maybe add a check when "slikts" is before "nav"
    new_fraze = fraze[:ir_nav] + "ir labs " + fraze[ir_slikts+6+1:]
    print(new_fraze)