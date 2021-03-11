import csv

# with open("test.csv", encoding="utf-8") as f:
#     my_data = [line.split(",") for line in f]
# print(my_data)

with open("test.csv", encoding="utf-8") as f:
    spamreader = csv.reader(f, delimiter=',', quotechar='"')
    my_csv_data = [row for row in spamreader]
    print(my_csv_data)

my_csv_data.append([5324,254524,24352])

with open("test-add.csv", mode="w",encoding="utf-8") as f:
    spamwriter = csv.writer(f, delimiter=';',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerows(my_csv_data)

# with open('eggs.csv', 'w', newline='') as csvfile:
#     spamwriter = csv.writer(csvfile, delimiter=' ',
#                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
#     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])