print("Esi sveicināts jautājumu spēlē par Latviju!")
question = input("Esi gatavs/a atbildēt uz jautājumiem par Latviju? (Jā/Nē): ")
score = 0
total = 20
 
# if question.lower() == "jā":
if "jā" in question.lower(): # ja jā ir kaut kur atbildē
    question =input("1.Kas ir Latvijas galvas pilsēta?")
    if question.lower() == "rīga":
        score += 1
        print ("Lielieski! Atbilde ir pareiza!")
    else:
        print ("Diemžēl, jūsu atbilde ir nepareiza! Pareizā atbilde - Rīga")
    
    question = input ("2.Kura ir Latvijas vecākā pilsēta?")
    if question.lower() == "Ludza":
        score += 1
        print ("Lielieski! Atbilde ir pareiza!")
    else:
        print ("Diemžēl, jūsu atbilde ir nepareiza! Pareizā atbilde - Ludza!")
    
    question = input ("3.Viens no lielākajiem meteorītu krāteriem Eiropā,atrodams tieši Latvijas teritorijā! Kurā pilsētā tas atrodas?")
    if question.lower == "Dobele" or question.lower() == "Dobelē":
        score += 1
        print ("Lielieski! Atbilde ir pareiza!")
    else:
        print ("Diemžēl, jūsu atbilde ir nepareiza! Pareizā atbilde - Dobele!")
        
    question = input ("4.Garākais tilts pār Daugavu Rīgā, kas būvēts kā Maskavas tilts no 1968. līdz 1976. gadam. Tā kopējais garums ir 3,5 km.?")
    if question.lower == "Salu tilts" or question.lower == "Salu":
        score += 1
        print ("Lielieski! Atbilde ir pareiza!")
    else:
        print ("Diemžēl, jūsu atbilde ir nepareiza! Pareizā atbilde - Salu tilts!")
        
    question = input ("5.Cik pilsētas šobrīd ir Latvijā?")
    if question.lower == "76":
        score += 1
        print ("Lielieski! Atbilde ir pareiza!")
    else:
        print ("Diemžēl, jūsu atbilde ir nepareiza! Pareizā atbilde - 76!")
        
    question = input ("6.Cik republikas nozīmju pilsētas ir Latvijā?")
    if question.lower == "9":
        score += 1
        print ("Lielieski! Atbilde ir pareiza!")
    else:
        print ("Diemžēl, jūsu atbilde ir nepareiza! Pareizā atbilde - 9!")
        
    question = input ("7.Kurā gadā, Latvija kļuva par pitmo postpadomju valsti, kura uzņēma NATO samitu?")
    if question.lower == "2006.gadā" or question.lower == "2006":
        score += 1
        print ("Lielieski! Atbilde ir pareiza!")
    else:
        print ("Diemžēl, jūsu atbilde ir nepareiza! Pareizā atbilde - 2006.gadā!")
        
    question = input ("8.Kurš ir populārākais sporta veids Latvijā?")
    if question.lower == "Hokejs":
        score += 1
        print ("Lielieski! Atbilde ir pareiza!")
    else:
        print ("Diemžēl, jūsu atbilde ir nepareiza! Pareizā atbilde - hokejs!")
        
    question = input ("9.Latvijas lielākais ezers?")
    if question.lower == "Lubānas ezers" or question.lower == "Lubānas":
        score += 1
        print ("Lielieski! Atbilde ir pareiza!")
    else:
        print ("Diemžēl, jūsu atbilde ir nepareiza! Pareizā atbilde - Lubānas ezers!")
        
    question = input ("10.Vienīgā un garākā upe, kas savu tecējumu sāk un beidz Latvijā?")
    if question.lower == "Gauja":
        score += 1
        print ("Lielieski! Atbilde ir pareiza!")
    else:
        print ("Diemžēl, jūsu atbilde ir nepareiza! Pareizā atbilde - Gauja!")
        
    question = input ("11.Kura atrodas vislielākā pils Latvijā, kuru uzcēla 1772. gadā, vēlīnā barokas stilā?")
    if question.lower == "Jelgavā":
        score += 1
        print ("Lielieski! Atbilde ir pareiza!")
    else:
        print ("Diemžēl, jūsu atbilde ir nepareiza! Pareizā atbilde - Jelgavā!")