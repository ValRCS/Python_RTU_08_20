# # 3. uzdevums
# txt = input("Input text: ")
# rev_txt = ' '.join(txt[::-1].split()[::-1]).capitalize()
# print(f"{txt} -> {rev_txt}")

#3.uzdevums
sentence = input("Ieraksti teikumu! : ")
words = sentence.split(" ")
reverse_words = [word[::-1] for word in words]
reverse_sentence = " ".join(reverse_words).capitalize()
print(f" Apgrieztie vārdi: {reverse_sentence}")