import math
import random

list=["a","b","c"]
q_geo=["The capital of Latvia is: a)Lisabon, b)Riga, c)Vilnius", "The largest ocean is: a)Atlantic, b)Indian, c)Silent", "The highest mountain in the world is: a)Everest, b)K2, c) Mont Blanc", "The deepest lake in the world: a) Rāznas, b)Baikal, c) Victoria", "The longest river in the wolrd is: a) Nile, b) Congo, c)Amazon"]
a_geo=["b", "c", "a", "b", "c" ]
q_poli=["The president of Spain:a)Diego Martínez, b)Manuel Azaña, c)Pedro Sánchez", "Who was president of Latvia (1999-2007):a) Vaira Vīķe-Freiberga, b)Kārlis Ulmanis c) Gustavs Zemgals", "American women voting rights back in: a)1890, b)1920, c)1935", "Which country is not a monarchy: a)Japan, b)Jordan, c) Ghana", "Greenland is an autonomous country within:a)USA, b)Great Britain c)Denmark"]
a_poli=["c","a","b","c","c"]
q_anim=["The longest snake in the world: a)>6m, b)>8m, c)>10m", "The biggest fish in the world: a)Tuna, b) whale shark, c)whale", "How many millions of years ago did Dinosaurs live: a)>22, b)>44, c)66", "Which animal was first domesticated: a) goat, b)cat, c)dog", "Which bird is symbol of peace: a)pigeon, b)dove, c)eagle"]
a_anim=["a","b","c","a","b"]
q_astr=["What is 3rd planet from the Sun: a)Earth, b)Mars, c)Venera", "The largest planet in Solar System: a)Jupiter, b)Saturn, c)Mercury", "When Yuri Gagarin went into outer space: a)1958, b)1968, c)1978", "The first person to walk on the Moon: a)Eugene Cernan, b)Neil Armstrong, c)Harrison Schmitt", "How many planets are in solar system:a)5, b)8, c)10"]
a_astr=["a","a","b","b","b"]
q_hist=["Who was the first ruler of the Mongol Empire: a)Togon-temür, b)Möngke Khan, c)Genghis Khan", "What year did India gain independence from Britain:a)1753, b)1895, c)1947", "What city was the first capital of the United States: a)Los Angeles, b)Washington, c)New York City", "What is the world's smallest country: a)Vatican City, b)San Marino, c)Monaco", "What nationality was Charlie Chaplin: a)British, b)American, c)German"]
a_hist=["c","c","c","a","a"]
q_big_list=[q_geo,q_poli,q_anim, q_astr, q_hist]
a_big_list=[a_geo,a_poli,a_anim, a_astr, a_hist]
money_total=0
money_q=250000
topics={1:"Geography", 2:"Politics", 3:"Animals", 4:"Astronomy", 5:"History"}
print("Hello, welcome to the VIZMA's game HOW TO BECOME MILLIONAIRE?")
print(f"Simple rules:\n1) you will have to choose 4 topics and answer 4 questions \n2) for each correct answer you get {money_q} and each wrong answer loose {money_q}\n3) Good Luck!")

for q in range(4):
    choice=int(input(f"Please choose one topic(write the number of the choice):{topics}"))
    while True:
        if choice in topics.keys():
            break
        else:
            print("Typing Error!!!")
            choice=int(input(f"Please choose one topic(write the number of the choice):{topics}"))
    print(f"Great choice-{topics[choice]}")
    topics.pop(choice)
    random_ch=random.randint(0,4)
    print("\n")
    print(f"Your question No.{q+1}\n{q_big_list[choice-1][random_ch]}")
    answer=input("Please type answer a, b or c?!")
    while True:
        if answer in list:
            break
        else:
            print("Typing Error!!!")
            answer=input("Please type answer a, b or c?!")
    if answer==a_big_list[choice-1][random_ch]:
        print(f"Great, you know it! You earned {money_q} Eur")
        money_total+=money_q
    else:
        print(f"Sorry, the answer is wrong, you lost {money_q} Eur! Correct was {a_big_list[choice-1][random_ch]}")
        money_total-=money_q
        
if money_total<=0:
    print("Sorry, you have not won money this time!")
elif money_total==1000000:
    print("Wohooo :) superhappy for you, you won {money_total}Eur! You are millionaire!")
else:
    print(f"Congratulations, you won {money_total} Eur")