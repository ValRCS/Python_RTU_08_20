#Piezīme: šads uzdevums kļuva populārs kā pirmais uzdevums, ko uzdot, lai noteiktu vai cilvēks vispār zina par programmēšanu :)
i=1
# number = int(input("Lūdzu ievadi skaitli "))
# number = 100
# while i <= number:
#     if i%5==0 and i%7==0:
#         print("FizzBuzz",end=',')
#     elif i%5==0:
#         print("Fizz",end=',')
#     elif i%7==0:
#         print("Buzz",end=',')
#     else:
#         print(i,end=',')
#     i+=1
# print("end code")

# 1. FizzBuzz
# Izdrukāt virknīti 1,2,3,4,Fizz,6,Buzz,8,.....34,FizzBuzz,36,....līdz  97,Buzz, 99,Fizz 
# Tātad ja skaitlis dalās ar 5 tad Fizz
# Ja dalās ar 7 tad Buzz,
# Ja dalās ar 5 UN 7 tad FizzBuzz
# savādāk pats skaitlis
 
fizz = 3
buzz = 5
fizz_text = "Fizz"
buzz_text = "Buzz"
end_sym = ","
final_sym = "\n"
start = 1
stop = 100
buffer = "" # alternative to printing is to save everything and print at end
 
for t in range(start, stop+1):
    end = end_sym if t != stop else final_sym # ternary expression
    # same as
#     if t != stop:
#         end = ", "
#     else:
#         end = ""
    if t % fizz == 0 and t % buzz == 0:
        print(fizz_text+buzz_text, end = end)
        buffer += fizz_text+buzz_text+end # f-strings would work just as well
        # note: for larget text segments concatation will get slow
        # alternatives are available
    elif t % fizz == 0:
        print(fizz_text, end = end)
        buffer += fizz_text+end
    elif t % buzz == 0:
        print(buzz_text, end = end)
        buffer += buzz_text+end
    else:
        print(t, end = end)
        buffer += f"{t}{end}" # or we could have cast t to str with str(t)
 
print(f"""
That's it, Fizzbuzzy task, hehe.
""")
print(buffer)