# uzd. 1.a
print("Input numbers to calculate average")
count = 1
total = 0.0
average = 0
number = 1
stopg = ""
while stopg != "q":
    number = float(input("Please enter number: "))
    total += number
    count += 1
    average = total/(count-1)
    print(round(average,2))
    stopg = input("To exit enter q  ")

#1c
# number_list = [45.0, 34.2, 10.3, 80.2]
number_list = []
while True:
    # print(number_list)
    query = input("Enter number or q to quit: ")
    if query == "q":
        print("Done with with work")
        break
    number_list.append(float(query))
    number_list.sort() #almost sorted list will be easy to sort
    print("Calculate their sum:")
    number_sum = sum(number_list)
    print(number_sum)
    print("Determine the length of the list:")
    number_len = len(number_list)
    print(number_len)
    print("Calculate their average:")
    avg = round(number_sum/number_len, 2)
    print(number_list[:3],avg,number_list[-3:])

