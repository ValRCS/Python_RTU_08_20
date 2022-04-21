'''
Atrodiet vai ievadītais veselais pozitīvais skaitlis ir pirmskaitlis.
 
Pirmskaitlis ir skaitlis, kas dalās bez atlikuma tikai pats ar sevi un 1.
 
Piezīme: šo uzdevumu var sākt risināt ļoti vienkārši un varat arī pēc tam optimizēt.
 
(kaut vai tas, ka mums nav jāpārbauda dalīšanās ar skaitļiem, kas lielāki par ievadītā skaitļa kvadrātsakni)
'''
 
number=(input("Enter digit for prime number testing (digits)\n"))
try:
    number_tested=int(number)
 
except ValueError:
    print("Error:")
    print("     You entered some letters")
 
for cur in range(2,int(number_tested**0.5)+1):  # in effect math.ceil
    if number_tested%cur==0 and cur<number_tested:
        print(f"Number {number_tested} is a not a prime number! It can be divided by {cur}")
        break
else: # runs when for loop ends with no breaks
    print(f"OMG!!! Number {number_tested} is a prime number!")