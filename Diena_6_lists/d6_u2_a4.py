#day6 ex2
while True:
    try:
        start = int(input('please enter a start number'))
    except ValueError:
        print('enter integer')
        continue
    break
while True:
    try:
        end = int(input('please enter a end number'))
 
    except ValueError:
        print('enter integer')
        continue
    break
if end > start:
    numbers = list(range(start, end, 1))
    kubi = [n**3 for n in numbers]
    print(f'{numbers} kubā {kubi}')
    # if we have two(or more) lists we can zip them together and loop through them
    for number, kubs in zip(numbers, kubi):
        print(f'{number} kubs ir {kubs}')