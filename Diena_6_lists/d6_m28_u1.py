print("Vidējā vērtība")
 
#num_len = int(input('Cik garš būs saraksts: '))
#count = 0
import statistics
new_list = []
average = None
while True: #num_len > count
    new_number = input('Ievadiet vērtību (q iziet): ')
    # if new_number.lower()[0] == 'q':
    if new_number.lower().startswith('q'):
        print('Darbs pabeigts!')
        break
    try:
        new_number = float(new_number)
        new_list.append(new_number)
        #average = round(sum(new_list)/len(new_list),2)
        average = round(statistics.mean(new_list),2)
        print(f'Ievadītie skaitļi {new_list}, vidējā vērtība: {average}')
    except ValueError:
        print('upps, jābūt skaitlim')   
sorted_list = sorted(new_list)
TOP3 = sorted_list[-3:][::-1]
BOTTOM3 = sorted_list[:3]
print(f'Saraksts: {new_list}')
print(f'Vidējā vērtība: {average}')
print(f'Mediana: {statistics.median(sorted_list)}') #mediana
print(f'Mode: {statistics.mode(sorted_list)}')  # most frequent value
print(f'TOP3: {TOP3}, BOTTOM3: {BOTTOM3}')
print()