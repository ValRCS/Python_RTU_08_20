# 3 uzdevums
 
sentence = input("Ievadi jebkādu teikumu!")
reversed_let = ' '.join(word[::-1] for word in sentence.split(" "))
print(reversed_let.capitalize())