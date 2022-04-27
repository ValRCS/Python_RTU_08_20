#1.a
#1.a. Frequency of symbols
text="hubba bubba"
def get_char_count(text):
    new_dict = {}
    for i in text:
        if i in new_dict:
            new_dict[i] +=1
        else:
            new_dict[i] = 1
    return new_dict
 
print(get_char_count(text))
print(get_char_count("Rīgā raibi runči rūķi "))

from collections import Counter

# #https://realpython.com/python-counter/
# Numbers=input(f"Enter a number: ") #.split()
# numbers = "1241245135236262626"
numbers = "12.3,412,451,352,362,626,26,26,26"
my_counter = Counter(numbers.split(","))
print(my_counter)
print(dict(my_counter)) # counter to dict

num = 1414515612626211135
print(Counter(str(num)))

#__________1uzd_____________
 
def get_char_count_2(text):
    text = str(text)
    dictionary = {}
    for letter in text:
        dictionary[letter] = text.count(letter)  # there is hidden loop in count
    return dictionary

print(get_char_count_2("Rīgā raibi runči rūķi "))

print(my_counter.most_common(10))

txt = """ASV aizsardzības sekretāra Loida Ostina (attēlā pa labi) komentārs, ka ASV vēlas redzēt Krieviju militāri novājinātu un nespējīgu ātri atgūties, iezīmē pavērsienu Vašingtonas deklarētajos mērķos, kas ir pamatā tās militārajam atbalstam Ukrainai, vēsta ziņu aģentūra “The Guardian”.

Preses konferencē Polijā, pēc vizītes Kijivā, Ostinam tika jautāts vai ASV mērķi šobrīd var tikt definēti citādāk, nekā tie, kas tika izvirzīti īsi pēc Krievijas iebrukuma sākuma. Atbildot viņš sāka ar jau iepriekš pausto administrācijas nostāju par palīdzību Ukrainai aizsargāt teritoriju un saglabāt tās suverenitāti. Tam sekoja piebilde par otru mērķi — ASV vēlas redzēt Krieviju militāri novājinātu līdz līmenim, kurā Maskava nevar veikt tādu iebrukumu, kāds pašreiz redzams Ukrainā, informēja "Sky News".

ASV valsts sekretārs Entonijs Blinkens, kurš kopā ar Ostinu bija Kijivā, piekrita Pentagona vadītāja formulējumam par ASV mērķiem.

Gan Ostina deifnētie mērķi, gan Blinkena paustā nostāja liecina, ka pat tad, ja Krievijas spēki aizietu no Ukrainas teritorijas vai tiktu sakauti, ASV un tās sabiedrotie censtos saglabāt sankcijas ar mērķi nepieļaut, ka Krievija atjauno spēkus un līdzīgu agresiju īsteno arī nākotnē, secina "The Guardian".

"Šobrīd runa nav tikai par Ukrainu; runa ir par lielāku problēmu, proti, draudiem, ko Krievija rada visai Eiropai", pauda politologs Rajans Menons.

"Aizsardzības sekretāra izteikumi bija patiesi, jo starptautiskās stabilitātes un Eiropas drošības interesēs ir tas, lai ar NATO valstīm nerobežojas militāri agresīva valsts," sacīja Eiropas Politikas analīzes centra priekšsēdētāja Alina Poļakova, kuru citē "The Guardian".

Taču šāda stratēģija rada zināmu risku. Ja Vladimirs Putins uzskatīs, ka viņa bruņotie spēki tiek iedzīti stūrī, viņš var pievērsties pastiprinātiem kiberuzbrukumiem Rietumu infrastruktūrai, ķīmiskajiem ieročiem vai arī taktisko kodolieroču arsenālam. Tā ir varbūtība, kas nebija iedomājama pirms astoņām nedēļām, bet tiek regulāri apspriesta šodien, secina laikraksts "The New York Times".

Centrālais jautājums par šo šķietami jauno Ostina stratēģiju ir saistīts ar tās spējām darboties praksē. Katra ASV administrācija kopš Harija Trumena ir ieviesusi plašas sankcijas pret Ziemeļkoreju, taču šobrīd Phenjanas rīcībā esošais kodolarsenāls ir lielāks kā jebkad. Donalds Tramps uzskatīja, ka sankcijām, ko viņš piemēroja Irānai, bija jāpanāk Islāma Republikas atgriešanās pie sarunu galda, tomēr šis scenārijs neīstenojās.

Džo Baidena administrācija signalizē, ka ar sankcijām vien nepietiks — tas, kas ir vajadzīgs, ir ļoti koordinēts sankciju, militārā spiediena un diplomātijas apvienojums. Tā kā šobrīd agresors ir Krievija, kas ir bruņota ar kodolieročiem, situācija un apstākļi ir daudz riskantāki, atzīmē "The New York Times "."""


letter_frequency = Counter(txt)
print(letter_frequency.most_common(10))
word_frequency = Counter(txt.split())
print(word_frequency.most_common(10))

