start = 1
stop = 100
fizz = 5
buzz = 7
fizz_text = "Fizzy"
buzz_text = "Buzzy"
end_char = ","

# we could also add everything to text buffer
text_buffer = ''
for num in range(start, stop+1):
    if num == stop:
        end_char = "\n"
    if num % fizz == 0 and num % buzz == 0:
        print(fizz_text+buzz_text, end=end_char) # f-strings would also work
        text_buffer += f"{fizz_text}{buzz_text}{end_char}"
    elif num % fizz == 0:
        print(fizz_text, end=end_char)
        text_buffer += f"{fizz_text}{end_char}"
    elif num % buzz == 0 :
        print(buzz_text, end=end_char)
        text_buffer += f"{buzz_text}{end_char}"
    else:
        print(num, end=end_char)
        text_buffer += f"{num}{end_char}"

# so we collected all text and only print at the end
print("*"*40)
print(text_buffer)
        ############
# Task Nr.1
############
# text = ''  # we create a text buffer
# for n in range(101):
#     if(n % 7 == 0 and n % 5 == 0):
#         text += 'FizzBuzz'
#     elif(n % 5 == 0):
#         text += 'Fizz'
#     elif(n % 7 == 0):
#         text += 'Buzz'
#     else:
#         text += str(n)
#     text += ","
# #     print(text, end=", ")
# print(text)
# print('\n')