def uzdevums_4():
    """
    Atrodiet un izvadiet pirmos 20 (vēl labāk iespēja izvēlēties cik pirmos pirmskaitļus gribam)
    pirmskaitļus saraksta veidā t.i. [2,3,5,7,11,...]
    """
    err_txt = "Pirmskaitļu skaitam jābūt > 1!"
    while True:
        try:
            user_input = int(input(f"Lūdzu, ievadiet cik pirmos pirmskaitļus nepieciešams atlasīt: "))
            if user_input and user_input > 0:
 
                def is_user_number_prime(k: int) -> bool:
                    """
                    :param k: Funkcija pieņem veselo pozitīvo skaitli
                    :return: True, ja skaitlis "k" IR pirmskaitlis; False, ja skaitlis "k" NAV pirmskaitlis
                    """
                    if k == 2 or k == 3:  # 2 un 3 ir pirmskaitli - uzreiz atgriežam True
                        return True
                    if not k % 2 or k < 2:  # 1 un pāru skaitli > 2 NAV pirmskaitli - uzreiz atgriežam False
                        return False
                    for i in range(3, int(k ** 0.5) + 1, 2):  # Pārbaudam tikai nepāra dalītājus sākot no 3
                        if not k % i:  # Ja "k" DALAS bez atlikuma uz kadu skaitli diapazonā no 3 līdz SQRT(k)
                            return False
                    return True
 
                cur_num, primes = 2, []
                while len(primes) < user_input:
                    if is_user_number_prime(cur_num):
                        primes.append(cur_num)
                    cur_num += 1
                print(f"Pirmie {user_input} pirmskaitļi: " + str(primes)[1:-1])
                break
        except ValueError:
            print(err_txt)

uzdevums_4()