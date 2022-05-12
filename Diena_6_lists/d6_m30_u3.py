# 3. Apgrieztie vārdi
# teikums_otradi=str()
# teikums=input("Lūdzu, ievadiet teikumu!")
# new_teikums=teikums.split()
# print(new_teikums)
# for i in new_teikums:
#     teikums_otradi +="".join(i[::-1])+' '
#     print(i[::-1])
#     print(teikums_otradi)

# Uzd3
# teikums = input("\nIevadi tekstu: ")
# teikums.lower()
# print(teikums.capitalize()," -> ",end=" ")

# vardi = teikums.split()
# for i in range(len(vardi)):
#   vardi[i]=vardi[i][::-1]
#   if not vardi[i][0].isalnum():
#     pieturzime = vardi[i][0]
#     vardi[i] = vardi[i][1:] + pieturzime

# print(" ".join(vardi).capitalize())

# 3. uzdevums
# - = - = - = - = - = - = - = - = - = - = - = - = 

 
teikums = input('Ievadi teikumu >> ')
 
pa_vardiem = teikums.split()

reversed_words = []
for word in pa_vardiem:
    reversed_words.append(word[::-1])
 
txt_reversed = " ".join(reversed_words)
# txt_reversed = " ".join([word[::-1] for word in pa_vardiem]) # same as above lines

 
print(txt_reversed.capitalize())