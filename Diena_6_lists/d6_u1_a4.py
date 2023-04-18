# Vidējā vērtība
numbers = []
while True:
    num = input("Ievadiet skaitli vai q, lai izietu: ")
    if num == "q":
        break
    try:
        num = float(num)
        numbers.append(num)
        avg = sum(numbers) / len(numbers)
        print(f"Vidējā vērtība: {avg}")
        print(f"Visi ievadītie skaitļi: {numbers}")
        top3 = sorted(numbers)[-3:][::-1]
        bottom3 = sorted(numbers)[:3]
        print(f"TOP3: {top3}")
        print(f"BOTTOM3: {bottom3}")
    except ValueError:
        print("Nepareiza ievade, lūdzu ievadiet skaitli vai q, lai izietu")