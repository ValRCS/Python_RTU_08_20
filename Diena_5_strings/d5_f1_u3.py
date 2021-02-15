# 3rd_Task
 
text = str(input("Please enter your text: "))
check_1 = "nav"
check_2 = "slikts"
change = "ir labs"
start = text.find(check_1)
end = text.find(check_2) + len(check_2)
if check_1 in text and check_2 in text and start < end:
    new_text = f"{text[:start]}{change}{text[end:]}"
    print(new_text)
else:
    print(text)